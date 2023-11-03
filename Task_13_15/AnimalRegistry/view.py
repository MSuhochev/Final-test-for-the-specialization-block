class View:
    @staticmethod
    def get_input(message):
        return input(message)

    @staticmethod
    def show_message(message):
        print(message)

    @staticmethod
    def invalid_choice():
        View.show_message("Некорректный ввод. Попробуйте еще раз.")
