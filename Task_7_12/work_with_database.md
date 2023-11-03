# """7"" 
        """Создать базу данных Friends_of_human"""
		
    CREATE DATABASE Friends_of_human;

        """Выбрать базу данных Friends_of_human"""
		
    USE Friends_of_human
	
        """Установить пользователя и пароль для БД Friends_of_human""
		
    ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'Swordfish';
	
        """перезагружаем сервер и применяем изменения"""
		
    FLUSH PRIVILEGES;
	
        """убеждаемся, что метод аутентификации изменен"""
		
    SELECT user,authentication_string,plugin,host FROM mysql.user;



# """8"""
       """Создать таблицы с иерархией из диаграммы в БД."""

CREATE TABLE Animals (
    animal_id INT AUTO_INCREMENT PRIMARY KEY,
    animal_name VARCHAR(100),
    animal_type VARCHAR(100),
    date_of_birth DATE,
    commands VARCHAR(100)
);

CREATE TABLE Pets (
    pet_id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT,
    pet_name VARCHAR(100),
    pet_type VARCHAR(100),
    date_of_birth DATE,
    commands VARCHAR(100),
    FOREIGN KEY (animal_id) REFERENCES Animals(animal_id)
);

CREATE TABLE PackAnimals (
    pack_animal_id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT,
    pack_animal_name VARCHAR(100),
    pack_animal_type VARCHAR(100),
    date_of_birth DATE,
    commands VARCHAR(100),
    FOREIGN KEY (animal_id) REFERENCES Animals(animal_id)
);

CREATE TABLE Dogs (
    dog_id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT,
    dog_name VARCHAR(100),
    dog_type VARCHAR(100),
    date_of_birth DATE,
    commands VARCHAR(100),
    FOREIGN KEY (pet_id) REFERENCES Pets(pet_id)
);

CREATE TABLE Cats (
    cat_id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT,
    cat_name VARCHAR(100),
    cat_type VARCHAR(100),
    date_of_birth DATE,
    commands VARCHAR(100),
    FOREIGN KEY (pet_id) REFERENCES Pets(pet_id)
);

CREATE TABLE Hamsters (
    hamster_id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT,
    hamster_name VARCHAR(100),
    hamster_type VARCHAR(100),
    date_of_birth DATE,
    commands VARCHAR(100),
    FOREIGN KEY (pet_id) REFERENCES Pets(pet_id)
);

CREATE TABLE Horses (
    horse_id INT AUTO_INCREMENT PRIMARY KEY,
    pack_animal_id INT,
    horse_name VARCHAR(100),
    horse_type VARCHAR(100),
    date_of_birth DATE,
    commands VARCHAR(100),
    FOREIGN KEY (pack_animal_id) REFERENCES PackAnimals(pack_animal_id)
);

CREATE TABLE Camels (
    camel_id INT AUTO_INCREMENT PRIMARY KEY,
    pack_animal_id INT,
    camel_name VARCHAR(100),
    camel_type VARCHAR(100),
    date_of_birth DATE,
    commands VARCHAR(100),
    FOREIGN KEY (pack_animal_id) REFERENCES PackAnimals(pack_animal_id)
);

CREATE TABLE Donkeys (
    donkey_id INT AUTO_INCREMENT PRIMARY KEY,
    pack_animal_id INT,
    donkey_name VARCHAR(100),
    donkey_type VARCHAR(100),
    date_of_birth DATE,
    commands VARCHAR(100),
    FOREIGN KEY (pack_animal_id) REFERENCES PackAnimals(pack_animal_id)
);

# """9"""
       """заполнение низкоуровневых таблиц именами(животных), командами, которые они выполняют, и датами рождения."""

INSERT INTO Animals (animal_name, animal_type, date_of_birth, commands) VALUES 
('Max', 'Dog', '2019-05-15', 'Sit, Stay, Fetch'),
('Simba', 'Cat', '2020-02-20', 'Meow, Jump'),
('Buddy', 'Hamster', '2022-01-10', 'Run, Eat');

INSERT INTO Pets (animal_id, pet_name, pet_type, date_of_birth, commands) VALUES 
(1, 'Max', 'Dog', '2019-05-15', 'Sit, Stay, Fetch'),
(2, 'Simba', 'Cat', '2020-02-20', 'Meow, Jump'),
(3, 'Buddy', 'Hamster', '2022-01-10', 'Run, Eat');

INSERT INTO Dogs (pet_id, dog_name, dog_type, date_of_birth, commands) VALUES 
(1, 'Max', 'Dog', '2019-05-15', 'Sit, Stay, Fetch');

INSERT INTO Cats (pet_id, cat_name, cat_type, date_of_birth, commands) VALUES 
(2, 'Simba', 'Cat', '2020-02-20', 'Meow, Jump');

INSERT INTO Hamsters (pet_id, hamster_name, hamster_type, date_of_birth, commands) VALUES 
(3, 'Buddy', 'Hamster', '2022-01-10', 'Run, Eat');

INSERT INTO Animals (animal_name, animal_type, date_of_birth, commands) VALUES 
('Rex', 'Horse', '2018-07-12', 'Gallop, Trot'),
('Coco', 'Camel', '2017-11-25', 'Carry, Walk'),
('Jack', 'Donkey', '2019-04-30', 'Carry, Pull');

INSERT INTO PackAnimals (animal_id, pack_animal_name, pack_animal_type, date_of_birth, commands) VALUES 
(4, 'Rex', 'Horse', '2018-07-12', 'Gallop, Trot'),
(5, 'Coco', 'Camel', '2017-11-25', 'Carry, Walk'),
(6, 'Jack', 'Donkey', '2019-04-30', 'Carry, Pull');

INSERT INTO Horses (pack_animal_id, horse_name, horse_type, date_of_birth, commands) VALUES 
(7, 'Rex', 'Horse', '2018-07-12', 'Gallop, Trot');

INSERT INTO Camels (pack_animal_id, camel_name, camel_type, date_of_birth, commands) VALUES 
(8, 'Coco', 'Camel', '2017-11-25', 'Carry, Walk');

INSERT INTO Donkeys (pack_animal_id, donkey_name, donkey_type, date_of_birth, commands) VALUES 
(9, 'Jack', 'Donkey', '2019-04-30', 'Carry, Pull');

# """10"""
        """Удалить из таблицы верблюдов"""
		
DELETE FROM Camels;

        """Объединить таблицы лошади, и ослы в одну таблицу.""""
		
SELECT * FROM Horses
UNION
SELECT * FROM Donkeys;

# """11"""
		"""Создаём новую таблицу “молодые животные” в которую попадают все животные старше 1 года, но младше 3 лет 
		   и в отдельном столбце с точностью до месяца подсчитываем возраст животных в новой таблице."""
		   
CREATE TABLE Young_Animals AS
SELECT *,
TIMESTAMPDIFF(MONTH, date_of_birth, CURDATE()) AS age_in_months
FROM Animals
WHERE date_of_birth BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

# """12"""
	    """Объединяем все таблицы в одну, при этом сохраняем поля, указывающие на прошлую принадлежность к старым таблицам."""
		
SELECT 'Animals' AS source_table, animal_id, animal_name, animal_type, date_of_birth, commands, NULL AS pet_id, NULL AS pet_name, NULL AS pet_type, NULL AS dog_id, NULL AS dog_name, NULL AS cat_id, NULL AS cat_name, NULL AS hamster_id, NULL AS hamster_name, NULL AS pack_animal_id, NULL AS pack_animal_name, NULL AS pack_animal_type, NULL AS horse_id, NULL AS horse_name, NULL AS camel_id, NULL AS camel_name, NULL AS donkey_id, NULL AS donkey_name
FROM Animals
UNION ALL
SELECT 'Pets', NULL, NULL, NULL, NULL, NULL, pet_id, pet_name, pet_type, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL
FROM Pets
UNION ALL
SELECT 'Dogs', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, dog_id, dog_name, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL
FROM Dogs
UNION ALL
SELECT 'Cats', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, cat_id, cat_name, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL
FROM Cats
UNION ALL
SELECT 'Hamsters', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, hamster_id, hamster_name, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL
FROM Hamsters
UNION ALL
SELECT 'PackAnimals', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, pack_animal_id, pack_animal_name, pack_animal_type, NULL, NULL, NULL, NULL, NULL, NULL
FROM PackAnimals
UNION ALL
SELECT 'Horses', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, horse_id, horse_name, NULL, NULL, NULL, NULL
FROM Horses
UNION ALL
SELECT 'Camels', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, camel_id, camel_name, NULL, NULL
FROM Camels
UNION ALL
SELECT 'Donkeys', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, donkey_id, donkey_name
FROM Donkeys;