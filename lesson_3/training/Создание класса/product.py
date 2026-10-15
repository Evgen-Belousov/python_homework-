class Product:
    # Конструктор: принимает имя и цену, сохраняет их в поля объекта
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Метод 1: возвращает название
    def get_name(self):
        return self.name

    # Метод 2: возвращает цену
    def get_price(self):
        return self.price

    # Метод 3: возвращает строку с информацией
    def get_info(self):
        return f"{self.name} - {self.price}"
