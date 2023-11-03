
from animal import Animal

# Класс AnimalController управляет взаимодействием между моделью и представлением.
class AnimalController:
    # Инициализируем контроллер с помощью экземпляров модели и представления.
    def __init__(self, model, view):
        self.model = model # Экземпляр модели (AnimalsRegistry)
        self.view = view # Экземпляр представления (AnimalView)

    # Метод add_animal добавляет в реестр новое животное на основе предоставленных данных.
    def add_animal(self, animal_name, animal_type, date_of_birth, commands):
        # Создаем экземпляр класса Animal.
        animal = Animal(animal_name, animal_type, date_of_birth, commands)
        # Добавляем животное в список модели животных.
        self.model.add_animal(animal)
        self.view.show_message(f"Животное {animal_name} добавлено в реестр.")

    # Метод list_commands извлекает и отображает список команд для конкретного животного.
    def list_commands(self, animal_name):
        # Получить команды для указанного животного.
        commands = self.model.db.get_animal_commands(animal_name)
        if commands:
            # Если команды найдены показать их.
            self.view.show_message(f"Команды для {animal_name}: {commands}")
        else:
            self.view.show_message(f"Животное с именем {animal_name} не найдено.")

    # Метод teach_command добавляет новую команду конкретному животному и отображает обновленный список команд.
    def teach_command(self, animal_name, new_command):
        # Добавьте новую команду к указанному животному.
        commands = self.model.teach_command(animal_name, new_command)
        if commands:
            # Если команда добавлена, отобразить их.
            self.view.show_commands(commands)
        else:
            self.view.show_message("Животное не найдено.")

    # метод удаления животного
    def remove_animal(self, animal_name):
        if self.model.remove_animal(animal_name):
            self.view.show_message(f"Животное с именем {animal_name} успешно удалено.")
            self.model.db.remove_animal_from_database(animal_name)
        else:
            self.view.show_message(f"Животное с именем {animal_name} не найдено.")
