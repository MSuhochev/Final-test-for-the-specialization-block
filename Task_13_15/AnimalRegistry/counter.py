class Counter:
    # Инициализируем
    def __init__(self):
        self.value = 0
        self.opened = False
    # Метод увеличивающий значение на 1
    def add(self):
        self.value += 1
    # Методы поддержки работы с объектом типа счетчик в блоке try-with-resources
    def __enter__(self):
        if self.opened:
            raise ValueError("Ресурс уже открыт")
        self.opened = True
        return self
    # Если работа с объектом происходит вне блока try-with-resources или если ресурс остается открытым, бросаем исключение
    def __exit__(self, exc_type, exc_value, traceback):
        if not self.opened:
            raise ValueError("Ресурс не был открыт")
        self.opened = False
