class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, amount):
        """увеличиваем скорость"""
        self.speed += amount
        return f'{self.brand} {self.model} {self.speed} разогналась до {self.speed} км/ч'

    def brake(self):
        """полная остановка"""
        self.speed = 0
        return f'{self.model} остановилась'

    def info(self):
        """информация о машине"""
        return f'{self.brand} {self.model}, год: {self.year}, скорость: {self.speed} км/ч'

"""создаем несколько машин"""
car1 = Car ('BMW','M5', 2024,)
car2 = Car ('Mercedes', 'AMG E63s', 2024)
car3 = Car ('Audi', 'RS6', 2023)

print(car1.info())
print(car1.accelerate(282))
print(car1.brake())
print("\n" + car2.info())
print(car2.accelerate(278))
print(car2.brake())
print("\n" + car3.info())
print(car3.accelerate(281))
print(car3.brake())









