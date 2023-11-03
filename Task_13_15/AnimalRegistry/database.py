import mysql.connector

# Класс для работы с базой данных
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Swordfish",
            database="Friends_of_human"
        )
        self.cursor = self.connection.cursor()

    # Добавить животное в базу данных
    def add_animal_to_database(self, animal_name, animal_type, date_of_birth, commands):
        query = "INSERT INTO Animals (animal_name, animal_type, date_of_birth, commands) VALUES (%s, %s, %s, %s)"
        values = (animal_name, animal_type, date_of_birth, ",".join(commands))  # Преобразование списка в строку
        self.cursor.execute(query, values)
        self.connection.commit()

    # Научить животное новой команде и записать её в БД
    def teach_animal_new_command(self, animal_name, new_command):
        query = "UPDATE Animals SET commands = CONCAT(commands, %s) WHERE animal_name = %s"
        values = (f",{new_command}", animal_name)
        self.cursor.execute(query, values)
        self.connection.commit()

    # Извлечь список всех животных из БД
    def get_all_animals(self):
        query = "SELECT * FROM Animals"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    # Извлечь список всех команд заданного животного из БД
    def get_animal_commands(self, animal_name):
        query = "SELECT commands FROM Animals WHERE animal_name = %s"
        self.cursor.execute(query, (animal_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    # Удалить животное из БД    
    def remove_animal_from_database(self, animal_name):
        query = "DELETE FROM Animals WHERE animal_name = %s"
        self.cursor.execute(query, (animal_name,))
        self.connection.commit()

    # Закрываем соединение с БД
    def __del__(self):
        self.connection.close()