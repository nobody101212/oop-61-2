class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f'{self.name} Готов к бою!'



class MageHero:
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)
        self.mp = mp

    def action(self):
        return f'Маг {self.name} Кастует заклинание! MP: {self.mp} '



class WarriorHero:
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)

    def action(self):
         return f'Воин {self.name} Рубит мечом! Уровень: {self.lvl}'

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







