class Hero:


    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибута класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
# объект/экземляр на основе класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero('Asuna', 101, 1001)

print(kirito.name)
print(asuna.name)