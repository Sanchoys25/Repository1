class BeautySalonExpert:
    def __init__(self):
        self.recommendations = []
    
    def start(self):
        print("\n" + "="*60)
        print("Добро пожаловать в экспертный систему салона красоты 'Лаванда'!")
        print("Мы поможем подобрать идеальную услугу для вас!")
        print("="*60)
        
        while True:
            self.show_menu()
            choice = input("\nВведите номер услуги (1-5) или '0' для выхода: ")
            
            if choice == '0':
                print("До свидания! Ждем вас в салоне 'Лаванда'!")
                break
            elif choice == '1':
                self.recommend_haircut()
            elif choice == '2':
                self.recommend_coloring()
            elif choice == '3':
                self.recommend_manicure()
            elif choice == '4':
                self.recommend_relax()
            elif choice == '5':
                self.recommend_full_look()
            else:
                print("Неверный выбор. Попробуйте еще раз.")
                continue
            
            self.show_recommendations()
            input("\nНажмите Enter чтобы продолжить...")
            self.recommendations = []  # Очищаем рекомендации для следующего выбора
    
    def show_menu(self):
        print("\n" + "-"*40)
        print("ВЫБЕРИТЕ УСЛУГУ:")
        print("1. Стрижка")
        print("2. Окрашивание")
        print("3. Маникюр")
        print("4. Расслабиться")
        print("5. Полный образ")
        print("0. Выход")
        print("-"*40)
    
    def recommend_haircut(self):
        print("\n--- ПОДБОР СТРИЖКИ ---")
        while True:
            answer = input("Вы хотите женскую стрижку или мужскую? (ж/м): ").lower()
            if answer == 'ж':
                self.recommendations.append({
                    'service': "Женская стрижка", 
                    'master': "Стилист-парикмахер", 
                    'price': "от 2000р.", 
                    'time': "1-1.5 часа",
                    'details': "С учетом укладки и консультации стилиста"
                })
                break
            elif answer == 'м':
                self.recommendations.append({
                    'service': "Мужская стрижка", 
                    'master': "Барбер", 
                    'price': "от 1000р.", 
                    'time': "45 минут",
                    'details': "С учетом стрижки и укладки"
                })
                break
            else:
                print("Пожалуйста, введите 'ж' или 'м'")
    
    def recommend_coloring(self):
        print("\n--- ПОДБОР ОКРАШИВАНИЯ ---")
        while True:
            answer = input("Вы хотите полное окрашивание или тонирование? (полное/тонирование): ").lower()
            if answer == 'полное':
                try:
                    budget = int(input("Ваш бюджет на окрашивание? (от 3000р.): "))
                    if budget >= 5000:
                        self.recommendations.append({
                            'service': "Сложное окрашивание с тонированием", 
                            'master': "Топ-колорист", 
                            'price': "5000-8000р.", 
                            'time': "3-4 часа",
                            'details': "С учетом сложной техники и премиальных материалов"
                        })
                    else:
                        self.recommendations.append({
                            'service': "Окрашивание в один тон", 
                            'master': "Парикмахер-колорист", 
                            'price': "3000-4500р.", 
                            'time': "2-3 часа",
                            'details': "Качественное окрашивание в выбранный оттенок"
                        })
                    break
                except ValueError:
                    print("Пожалуйста, введите число")
            elif answer == 'тонирование':
                self.recommendations.append({
                    'service': "Тонирование/мелирование", 
                    'master': "Колорист", 
                    'price': "от 4000р.", 
                    'time': "2.5-3.5 часа",
                    'details': "Щадящее окрашивание с эффектом мелирования"
                })
                break
            else:
                print("Пожалуйста, введите 'полное' или 'тонирование'")
    
    def recommend_manicure(self):
        print("\n--- ПОДБОР МАНИКЮРА ---")
        while True:
            answer = input("Вам нужен классический или аппаратный маникюр? (классический/аппаратный): ").lower()
            if answer == 'классический':
                self.recommendations.append({
                    'service': "Классический маникюр + покрытие", 
                    'master': "Мастер ногтевого сервиса", 
                    'price': "2500р.", 
                    'time': "1.5 часа",
                    'details': "Аккуратный маникюр с покрытием гель-лаком"
                })
                break
            elif answer == 'аппаратный':
                self.recommendations.append({
                    'service': "Аппаратный маникюр + покрытие", 
                    'master': "Мастер ногтевого сервиса", 
                    'price': "3000р.", 
                    'time': "1.5 часа",
                    'details': "Современный аппаратный маникюр с точной обработкой"
                })
                break
            else:
                print("Пожалуйста, введите 'классический' или 'аппаратный'")
    
    def recommend_relax(self):
        print("\n--- ПОДБОР РЕЛАКСА ---")
        while True:
            answer = input("Вам нужен массаж или спа-процедуры? (массаж/спа): ").lower()
            if answer == 'массаж':
                self.recommendations.append({
                    'service': "Расслабляющий массаж всего тела", 
                    'master': "Массажист", 
                    'price': "3500р.", 
                    'time': "1.5 часа",
                    'details': "Профессиональный массаж для расслабления и снятия напряжения"
                })
                break
            elif answer == 'спа':
                self.recommendations.append({
                    'service': "СПА-уход для лица с массажем", 
                    'master': "Косметолог", 
                    'price': "4500р.", 
                    'time': "2 часа",
                    'details': "Комплексный уход за лицом с массажем и масками"
                })
                break
            else:
                print("Пожалуйста, введите 'массаж' или 'спа'")
    
    def recommend_full_look(self):
        print("\n--- ПОДБОР ПОЛНОГО ОБРАЗА ---")
        try:
            time = int(input("Сколько часов у вас есть? (рекомендуем 4-5 часов): "))
            budget = int(input("Какой бюджет готовы выделить? (от 7000р.): "))
            
            if budget >= 10000 and time >= 5:
                self.recommendations.append({
                    'service': "Премиум-образ: стрижка, окрашивание, маникюр, макияж", 
                    'master': "Команда мастеров", 
                    'price': "10000-15000р.", 
                    'time': "5-6 часов",
                    'details': "Полное преображение с участием топ-мастеров"
                })
            elif budget >= 7000 and time >= 4:
                self.recommendations.append({
                    'service': "Полный образ: стрижка, окрашивание, маникюр", 
                    'master': "Команда мастеров", 
                    'price': "7000-9000р.", 
                    'time': "4-5 часов",
                    'details': "Комплекс услуг для создания завершенного образа"
                })
            else:
                self.recommendations.append({
                    'service': "Базовый образ: стрижка и маникюр", 
                    'master': "Парикмахер и мастер маникюра", 
                    'price': "4000-5000р.", 
                    'time': "2.5-3 часа",
                    'details': "Отличный вариант для быстрого преображения"
                })
                self.recommendations.append({
                    'service': "Рекомендация", 
                    'master': "", 
                    'price': "", 
                    'time': "",
                    'details': "Для полного образа рекомендуем бюджет от 7000р. и 4-5 часов времени"
                })
                
        except ValueError:
            print("Будет выбран базовый вариант")
            self.recommendations.append({
                'service': "Базовый образ: стрижка и маникюр", 
                'master': "Парикмахер и мастер маникюра", 
                'price': "4000-5000р.", 
                'time': "2.5-3 часа",
                'details': "Отличный вариант для быстрого преображения"
            })
    
    def show_recommendations(self):
        print("\n" + "="*60)
        print("РЕКОМЕНДАЦИИ САЛОНА 'ЛАВАНДА':")
        print("="*60)
        
        if not self.recommendations:
            print("К сожалению, не удалось подобрать услугу.")
        else:
            for i, rec in enumerate(self.recommendations, 1):
                print(f"\n--- Вариант {i} ---")
                print(f"Услуга: {rec['service']}")
                print(f"Мастер: {rec['master']}")
                print(f"Стоимость: {rec['price']}")
                print(f"Время: {rec['time']}")
                print(f"Описание: {rec['details']}")
        
        print("\n" + "="*60)
        print("Записаться на услугу можно по телефону: +7 (495) 123-45-67")
        print("Наши адреса: Москва, ул. Пушкинская, д. 10 и г. Мытищи")
        print("="*60)

# Запуск программы
if __name__ == "__main__":
    expert = BeautySalonExpert()
    expert.start()
