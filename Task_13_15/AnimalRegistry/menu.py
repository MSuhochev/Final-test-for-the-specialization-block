from switch_case import SwitchCase


class Menu:
    @staticmethod
    def start_menu(view, controller):
        while True:
            view.show_message("1. Завести новое животное")
            view.show_message("2. Определить животное в правильный класс")
            view.show_message("3. Показать список команд животного")
            view.show_message("4. Обучить животное новой команде")
            view.show_message("5. Выйти из программы")

            choice = view.get_input("Выберите действие: ")

            switch_case = SwitchCase()
            switch_case.choose_action(choice, controller, view)