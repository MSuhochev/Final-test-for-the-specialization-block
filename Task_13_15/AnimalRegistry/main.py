
from animal_view import AnimalView
from animal_registry import AnimalsRegistry
from animal_controller import AnimalController
from database import Database
from menu_handler import Handler

if __name__ == '__main__':
    # Инициализируем экземпляр класса AnimalView.
    view = AnimalView()
    # Инициализируем экземпляр класса базы данных для взаимодействия с базой данных.
    db = Database()
    # Инициализируем экземпляр класса AnimalsRegistry с помощью экземпляра базы данных.
    model = AnimalsRegistry(db)
    # Инициализируем экземпляр класса AnimalController с экземплярами модели и представления.
    controller = AnimalController(model, view)
    
    # Запускаем основной цикл приложения.
    while True:
        # Отображаем меню и получаем выбор пользователя.
        choice = view.show_menu()
        # Проверяем, должна ли выбранная опция выйти из программы, и при необходимости разрываем цикл.
        if not Handler.handle_menu_choice(choice, controller, db, view):
            break