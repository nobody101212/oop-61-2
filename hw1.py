# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, amount):
#         """увеличиваем скорость"""
#         self.speed += amount
#         return f'{self.brand} {self.model} {self.speed} разогналась до {self.speed} км/ч'
#
#     def brake(self):
#         """полная остановка"""
#         self.speed = 0
#         return f'{self.model} остановилась'
#
#     def info(self):
#         """информация о машине"""
#         return f'{self.brand} {self.model}, год: {self.year}, скорость: {self.speed} км/ч'
#
# """создаем несколько машин"""
# car1 = Car ('BMW','M5', 2024,)
# car2 = Car ('Mercedes', 'AMG E63s', 2024)
# car3 = Car ('Audi', 'RS6', 2023)
#
# print(car1.info())
# print(car1.accelerate(282))
# print(car1.brake())
# print("\n" + car2.info())
# print(car2.accelerate(278))
# print(car2.brake())
# print("\n" + car3.info())
# print(car3.accelerate(281))
# print(car3.brake())

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f'{self.name} готов к бою!'



class MageHero:
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f'Маг {self.name} кастует заклинание! MP: {self.mp} '



class WarriorHero:
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)

    def action(self):
         return f'Воин {self.name} рубит мечом! Уровень: {self.lvl}'

class BankAccount:
    def __init__(self, hero, bank_name, login, password):
        self.hero = hero
        self.bank = bank_name
        self._login = login
        self.__password = password
    def login(self, password):
         return password == self.__password
    @property
    def full_info(self):
        return f"Герой: {self.hero.name}, Уровень: {self.hero.lvl}, Баланс: {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f'{self.hero.name} | Баланс: {self.balance} SOM'

    def __add__(self, other ):
        if type (self.hero) is not type(other.hero):
            raise TypeError('нельзя сложить героев счета разных классов!')
        return self._balance+ other._balance

    def __eq__(self, other ):
        return (
            self.hero.name == other.hero.name and
            self.hero.lvl == other.hero.lvl
        )
from abc import ABC, abstractmethod
class SmsService(ABC):

    @abstractmethod
    def send_otp(self, phone):
        pass
class KGSms(SmsService):
    def send_otp(self, phone):
        return f'<text>Код: 1234</text><phone>{phone}</phone>'

class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234","phone": phone}

mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)

acc1 = BankAccount(mage1, 5000, '1234', 'simba')
acc2 = BankAccount(mage2, 3000, '1111', 'simba')
acc3 = BankAccount(warrior, 2500, '1111', 'simba')

print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc2.bonus_for_level(), "SOM")
print("\n=== Проверка__add__===")
print("Сумма счетов двух магов:", acc1 + acc2)

try:
    print("Cумма мага и воина:", acc1 = acc3)
except Exception as e:
    print("Ошибка:", e)

print('\n=== Проверка __eq__===')
print('Mage1 == Mage2 ?', acc1 == acc2)
print('Mage1 == Warrior ?', acc1 == acc3)

sms = KGSms()
print("\n", sms.send_otp('+996777123456'))









