from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from db import db
from models import User, Post, Comment
from forms import RegistrationForm, LoginForm, PostForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Инициализация Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    posts = Post.query.filter_by(is_private=False).all()  # Показываем только публичные посты
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Генерация хеша пароля
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        tags = form.tags.data
        is_private = request.form.get('is_private') == 'on'  # Получаем значение чекбокса
        new_post = Post(title=title, content=content, user_id=current_user.id, tags=tags, is_private=is_private)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully!')
        return redirect(url_for('home'))
    return render_template('create_post.html', form=form)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author.id != current_user.id:
        flash('You cannot edit this post.')
        return redirect(url_for('home'))

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.tags = form.tags.data
        db.session.commit()
        flash('Post updated successfully!')
        return redirect(url_for('view_post', post_id=post.id))

    # Pre-fill the form with the current post data
    form.title.data = post.title
    form.content.data = post.content
    form.tags.data = post.tags
    return render_template('edit_post.html', form=form, post=post)

@app.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author.id != current_user.id:
        flash('You cannot delete this post.')
        return redirect(url_for('home'))

    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!')
    return redirect(url_for('home'))

@app.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user=user)

@app.route('/subscribe/<int:user_id>', methods=['POST'])
@login_required
def subscribe(user_id):
    user = User.query.get_or_404(user_id)
    if user in current_user.subscriptions:
        flash('You are already subscribed to this user.')
    else:
        current_user.subscriptions.append(user)
        db.session.commit()
        flash('You have successfully subscribed to {}.'.format(user.username))
    return redirect(url_for('profile', user_id=user.id))

@app.route('/unsubscribe/<int:user_id>', methods=['POST'])
@login_required
def unsubscribe(user_id):
    user = User.query.get_or_404(user_id)
    if user not in current_user.subscriptions:
        flash('You are not subscribed to this user.')
    else:
        current_user.subscriptions.remove(user)
        db.session.commit()
        flash('You have successfully unsubscribed from {}.'.format(user.username))
    return redirect(url_for('profile', user_id=user.id))

@app.route('/search_by_tag')
def search_by_tag():
    tag = request.args.get('tag')
    posts = Post.query.filter(Post.tags.like(f'%{tag}%')).all()  # Поиск по тегам
    return render_template('index.html', posts=posts)

@app.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form['content']
    
    # Создаем новый комментарий
    new_comment = Comment(content=content, post_id=post.id, user_id=current_user.id)
    db.session.add(new_comment)
    db.session.commit()
    
    flash('Comment added successfully!')
    return redirect(url_for('view_post', post_id=post.id))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создайте таблицы
    app.run(debug=True)