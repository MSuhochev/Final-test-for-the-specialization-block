# Класс Animal представляет собой обычное животное с базовыми атрибутами.
class Animal:
    def __init__(self, animal_name, animal_type, date_of_birth, commands):
        self.animal_name = animal_name
        self.animal_type = animal_type
        self.date_of_birth = date_of_birth
        self.commands = commands

# Класс Pets представляет особый тип Animal, который включает в себя дополнительные атрибуты, связанные с домашними животными.
class Pets(Animal):
    def __init__(self, animal_name, animal_type, date_of_birth, commands, pet_name, pet_type):
        super().__init__(animal_name, animal_type, date_of_birth, commands)
        self.pet_name = pet_name
        self.pet_type = pet_type

# Класс PackAnimals представляет особый тип Animal, который можно использовать в качестве вьючного животного, с дополнительными атрибутами, связанными с вьючными животными.
class PackAnimals(Animal):
    def __init__(self, animal_name, animal_type, date_of_birth, commands, pack_animal_name, pack_animal_type):
        super().__init__(animal_name, animal_type, date_of_birth, commands)
        self.pack_animal_name = pack_animal_name
        self.pack_animal_type = pack_animal_type

# Класс Dogs представляет особый тип домашних животных с дополнительными атрибутами, связанными с собаками.
class Dogs(Pets):
    def __init__(self, animal_name, animal_type, date_of_birth, commands, pet_name, pet_type, dog_name, dog_type):
        super().__init__(animal_name, animal_type, date_of_birth, commands, pet_name, pet_type)
        self.dog_name = dog_name
        self.dog_type = dog_type

# Класс Cats представляет особый тип домашних животных с дополнительными атрибутами, связанными с кошками.
class Cats(Pets):
    def __init__(self, animal_name, animal_type, date_of_birth, commands, pet_name, pet_type, cat_name, cat_type):
        super().__init__(animal_name, animal_type, date_of_birth, commands, pet_name, pet_type)
        self.cat_name = cat_name
        self.cat_type = cat_type

# Класс Hamsters представляет особый тип домашних животных с дополнительными атрибутами, связанными с хомяками.
class Hamsters(Pets):
    def __init__(self, animal_name, animal_type, date_of_birth, commands, pet_name, pet_type, hamster_name, hamster_type):
        super().__init__(animal_name, animal_type, date_of_birth, commands, pet_name, pet_type)
        self.hamster_name = hamster_name
        self.hamster_type = hamster_type

# Класс Horses представляет особый тип PackAnimal с дополнительными атрибутами, связанными с лошадьми.
class Horses(PackAnimals):
    def __init__(self, animal_name, animal_type, date_of_birth, commands, pack_animal_name, pack_animal_type, horse_name, horse_type):
        super().__init__(animal_name, animal_type, date_of_birth, commands, pack_animal_name, pack_animal_type)
        self.horse_name = horse_name
        self.horse_type = horse_type

# Класс Camels представляет особый тип PackAnimal с дополнительными атрибутами, связанными с верблюдами.
class Camels(PackAnimals):
    def __init__(self, animal_name, animal_type, date_of_birth, commands, pack_animal_name, pack_animal_type, camel_name, camel_type):
        super().__init__(animal_name, animal_type, date_of_birth, commands, pack_animal_name, pack_animal_type)
        self.camel_name = camel_name
        self.camel_type = camel_type

# Класс Donkeys представляет особый тип PackAnimal с дополнительными атрибутами, связанными с ослами.
class Donkeys(PackAnimals):
    def __init__(self, animal_name, animal_type, date_of_birth, commands, pack_animal_name, pack_animal_type, donkey_name, donkey_type):
        super().__init__(animal_name, animal_type, date_of_birth, commands, pack_animal_name, pack_animal_type)
        self.donkey_name = donkey_name
        self.donkey_type = donkey_type






