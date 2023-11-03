
from counter import Counter


class Handler():

    # Метод принимает выбор пользователя и выполняет соответствующие действия.
    def handle_menu_choice(choice, controller, db, view):
        newcounter = Counter()

        # Выбор 1 позволяет пользователю добавить новое животное в реестр и базу данных.
        if choice == '1':
            try:
                with newcounter as counter:
                    animal_name = input("Введите имя животного: ")
                    animal_type = input("Введите тип животного: ")
                    date_of_birth = input("Введите дату рождения животного: ")
                    commands = input("Введите список команд через запятую: ").split(',')
                    # Вызываем метод контроллера, чтобы добавить животное.
                    controller.add_animal(animal_name, animal_type, date_of_birth, commands)
                    # Вызываем метод базы данных для хранения данных в БД.
                    db.add_animal_to_database(animal_name, animal_type, date_of_birth, commands)
                    if animal_name and animal_type and date_of_birth and commands:
                        counter.add()  # Увеличивает значение счетчика на 1 при заполненных полях
                    # Другие операции с объектом Счетчик
                    else:
                        raise ValueError("Заполните все поля для животного.")
            except ValueError as e:
                print(f"Ошибка: {e}")  # Вывод сообщения об ошибке, если поля не заполнены
        # Выбор 2 позволяет пользователю перечислить все команды конкретного животного.
        elif choice == '2':
            animal_name = input("Введите имя животного: ")
            controller.list_commands(animal_name)
        # Выбор 3 позволяет пользователю обучить новой команде конкретное животное.
        elif choice == '3':
            animal_name = input("Введите имя животного: ")
            new_command = input("Введите новую команду: ")
            controller.teach_command(animal_name, new_command)
            db.teach_animal_new_command(animal_name, new_command)
            view.show_message(f"Новая команда '{new_command}' добавлена для {animal_name} и сохранена в базе данных.")
        # Выбор 4 извлекает всех животных из базы данных и отображает их данные.
        elif choice == '4':
            animals = db.get_all_animals()
            # Если животные найдены, отображаем их данные.
            if animals:
                for animal in animals:
                    view.show_message(f"Animal ID: {animal[0]}, Name: {animal[1]}, Type: {animal[2]}, Date of Birth: {animal[3]}, Commands: {animal[4]}")
            else:
                view.show_message("Животные не найдены в базе данных.")
        
        # Выбор 5 позволяет пользователю удалить животное.
        if choice == '5':
            animal_name = input("Введите имя животного для удаления: ")
            controller.remove_animal(animal_name)

        # Выбор 0 позволяет пользователю выйти из программы.
        elif choice == '0':
            return False
        else:
            view.show_message("Неверный выбор. Пожалуйста, выберите снова.")
        return True