class AnimalsRegistry:
  
    # Список уровня класса для хранения всех экземпляров животных, используется всеми экземплярами класса
    animals_list = []

    def __init__(self, db):
        self.animals = [] # Список уровня экземпляра для хранения отдельных экземпляров животных
        self.db = db # Экземпляр базы данных

    

    @classmethod
    # Метод класса для добавления нового животного в список уровня класса
    def add_animal(cls, animal):
        cls.animals_list.append(animal)

    @classmethod
    # Метод класса для вывода списка команд конкретного животного
    def list_commands(cls, animal_name):
        for animal in cls.animals_list:
            if animal.animal_name == animal_name:
                return animal.commands

    @classmethod
    # Метод класса для обучения новой команде конкретного животного
    def teach_command(cls, animal_name, new_command):
        for animal in cls.animals_list:
            if animal.animal_name == animal_name:
                animal.commands.append(new_command)
                return animal.commands
            
    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.get_name() == animal_name:
                self.animals.remove(animal)
                return True
        return False

