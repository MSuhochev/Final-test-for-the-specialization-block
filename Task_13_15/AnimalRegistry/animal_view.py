# Класс AnimalView предоставляет методы для отображения информации пользователю.
class AnimalView:
    # Метод show_menu отображает пользователю параметры главного меню и возвращает выбор пользователя.
    def show_menu(self):
        print("1. Завести новое животное")
        print("2. Показать список команд для животного")
        print("3. Обучить животное новым командам")
        print("4. Вывести список всех животных")
        print("5. Удалить животное")
        print("0. Выйти из программы")
        choice = input("Выберите опцию (1/2/3/4/5/0): ")
        return choice

    # Метод show_commands отображает пользователю список команд для конкретного животного.
    def show_commands(self, commands):
        print(f"Commands: {commands}")

    # Метод show_message отображает сообщение пользователю.
    def show_message(self, message):
        print(message)
