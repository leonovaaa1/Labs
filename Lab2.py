from abc import ABC, abstractmethod


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


class GameObject(ABC):
    def __init__(self, id, name, x, y):
        self._id = id
        self._name = name
        self._x = x
        self._y = y

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    @abstractmethod
    def describe(self):
        pass


class Unit(GameObject):
    def __init__(self, id, name, x, y, hp):
        super().__init__(id, name, x, y)
        self._hp = hp

    def is_alive(self):
        return self._hp > 0

    def get_hp(self):
        return self._hp

    def receive_damage(self, damage):
        self._hp = max(0, self._hp - damage)

    def describe(self):
        return f"Юнит {self._name}, HP={self._hp}"


class Building(GameObject):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y)
        self._built = built

    def is_built(self):
        return self._built

    def describe(self):
        return f"Постройка {self._name}, построена: {self._built}"


class Archer(Unit, Attacker, Moveable):
    def attack(self, unit):
        unit.receive_damage(10)

    def move(self, x, y):
        self._x = x
        self._y = y


class Fort(Building, Attacker):
    def attack(self, unit):
        unit.receive_damage(30)


class MobileHome(Building, Moveable):
    def move(self, x, y):
        self._x = x
        self._y = y


archer = Archer(1, "Робин", 0, 0, 50)
enemy = Archer(2, "Враг", 5, 5, 25)
fort = Fort(3, "Крепость", 10, 10, True)
home = MobileHome(4, "Караван", 2, 2, False)

archer.attack(enemy)
print("HP врага после лучника:", enemy.get_hp())

fort.attack(enemy)
print("HP врага после крепости:", enemy.get_hp(), "| жив:", enemy.is_alive())

archer.move(3, 4)
print("Лучник теперь в:", archer.get_x(), archer.get_y())

home.move(9, 9)
print("Дом теперь в:", home.get_x(), home.get_y())

for obj in (archer, enemy, fort, home):
    print(obj.describe())