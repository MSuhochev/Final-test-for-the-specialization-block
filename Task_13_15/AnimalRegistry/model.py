class Animals:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

class PackAnimals(Animals):
    def __init__(self, name, animal_type, commands):
        super().__init__(name, animal_type)
        self.commands = commands

    def add_command(self, command):
        self.commands.append(command)

    def show_commands(self):
        print(f"Список команд для {self.name}:")
        for command in self.commands:
            print(f"- {command}")

class Horse(PackAnimals):
    def __init__(self, name, commands):
        super().__init__(name, "horse", commands)

class Camel(PackAnimals):
    def __init__(self, name, commands):
        super().__init__(name, "camel", commands)

class Donkey(PackAnimals):
    def __init__(self, name, commands):
        super().__init__(name, "donkey", commands)

class PetAnimals(Animals):
    def __init__(self, name, commands):
        super().__init__(name, "pet")
        self.commands = commands

    def add_command(self, command):
        self.commands.append(command)

    def show_commands(self):
        print(f"Список команд для {self.name}:")
        for command in self.commands:
            print(f"- {command}")

class Dog(PetAnimals):
    def __init__(self, name, commands):
        super().__init__(name, commands)

class Cat(PetAnimals):
    def __init__(self, name, commands):
        super().__init__(name, commands)

class Hamster(PetAnimals):
    def __init__(self, name, commands):
        super().__init__(name, commands)
