from model import Horse, Dog, Cat, Hamster, Camel, Donkey
from view import View

class Controller:
    def __init__(self):
        self.animal_registry = []

    def add_animal(self):
    
        animal_name = input("Введите имя нового животного: ")
        animal_type = input("Введите тип животного (dog, cat, hamster и т.д.): ")

        if animal_type.lower() == 'dog':
            animal = Dog(animal_name, [])
        elif animal_type.lower() == 'cat':
            animal = Cat(animal_name, [])
        elif animal_type.lower() == 'hamster':
            animal = Hamster(animal_name, [])
        else:
            print("Некорректный тип животного.")
        return
    
    def define_animal_class():
        animal_name = input("Введите имя животного: ")
        animal_type = input("Введите тип животного: ")

        if animal_type.lower() == 'dog':
            print(f"{animal_name} принадлежит к классу собак.")
        elif animal_type.lower() == 'cat':
            print(f"{animal_name} принадлежит к классу кошек.")
        elif animal_type.lower() == 'hamster':
            print(f"{animal_name} принадлежит к классу хомяков.")
        else:
            print("Не удалось определить класс для данного типа животного.")

    def show_animal_commands(self):
        # Реализуйте логику показа списка команд животного
        pass

    def train_animal(self):
        # Реализуйте логику обучения животного новой команде
        pass

    def exit_program(self):
        quit()
