from abc import ABC, abstractmethod
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} создает идеальный куб! MP: {self.mp}"


# Warrior наследует MageHero
class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        return f"Воин {self.name} рубит Риттой! Уровень: {self.lvl}"


class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self.bank_name = bank_name
        self._balance = balance
        self.__password = password

    def login(self, password):
        return password == self.__password

    @property
    def full_info(self):
        return f"{self.hero.name} | Лвл: {self.hero.lvl} | Баланс: {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) is not type(other.hero):
            raise TypeError("Нельзя сложить счета героев разных классов!")
        return self._balance + other._balance

    def __eq__(self, other):
        return (
            self.hero.name == other.hero.name and
            self.hero.lvl == other.hero.lvl
        )


class SmsService(ABC):

    @abstractmethod
    def send_otp(self, phone):
        pass


class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"


class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}

mage1 = MageHero("Gowther", 3000, 900, 1250)
mage2 = MageHero("Merlin", 3000, 1000, 1120)
warrior = WarriorHero("Escanor", 40, 120000, 100000)


acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")


print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")
print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)
try:
    print("Сумма мага и воина:", acc1 + acc3)
except Exception as e:
    print("Ошибка:", e)

print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

sms = KGSms()
print("\n", sms.send_otp("+996777123456"))
