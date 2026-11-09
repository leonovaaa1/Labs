from abc import ABC, abstractmethod


class Settings:
    _instance = None

    def __init__(self):
        self.language = "ru"
        self.theme = "light"

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


class Notification(ABC):
    @abstractmethod
    def send(self, message): ...


class EmailNotification(Notification):
    def send(self, message):
        print("Отправлено по e-mail: " + message)


class SmsNotification(Notification):
    def send(self, message):
        print("Отправлено по SMS: " + message)


class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        ...

    def notify(self, message):
        notification = self.create_notification()
        notification.send(message)


class EmailFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()


class SmsFactory(NotificationFactory):
    def create_notification(self):
        return SmsNotification()


class Chair(ABC):
    @abstractmethod
    def show(self): ...


class ModernChair(Chair):
    def show(self):
        print("Современный стул: металл и пластик.")


class ClassicChair(Chair):
    def show(self):
        print("Классический стул: резное дерево.")


class Table(ABC):
    @abstractmethod
    def show(self): ...


class ModernTable(Table):
    def show(self):
        print("Современный стол: стекло и металл.")


class ClassicTable(Table):
    def show(self):
        print("Классический стол: массив дуба.")


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self): ...

    @abstractmethod
    def create_table(self): ...


class ModernFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()


class ClassicFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()

    def create_table(self):
        return ClassicTable()


class Room:
    def __init__(self, factory):
        self.chair = factory.create_chair()
        self.table = factory.create_table()

    def show(self):
        self.chair.show()
        self.table.show()


class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.sauce = None

    def __str__(self):
        return f"Burger(bun='{self.bun}', patty='{self.patty}', sauce='{self.sauce}')"


class BurgerBuilder(ABC):
    @abstractmethod
    def build_bun(self): ...

    @abstractmethod
    def build_patty(self): ...

    @abstractmethod
    def build_sauce(self): ...

    @abstractmethod
    def get_result(self): ...


class BeefBurgerBuilder(BurgerBuilder):
    def __init__(self):
        self.burger = Burger()

    def build_bun(self):
        self.burger.bun = "с кунжутом"

    def build_patty(self):
        self.burger.patty = "говяжья котлета"

    def build_sauce(self):
        self.burger.sauce = "барбекю"

    def get_result(self):
        return self.burger


class VeggieBurgerBuilder(BurgerBuilder):
    def __init__(self):
        self.burger = Burger()

    def build_bun(self):
        self.burger.bun = "цельнозерновая"

    def build_patty(self):
        self.burger.patty = "овощная котлета"

    def build_sauce(self):
        self.burger.sauce = "йогуртовый"

    def get_result(self):
        return self.burger


class BurgerDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_burger(self):
        self.builder.build_bun()
        self.builder.build_patty()
        self.builder.build_sauce()


if __name__ == "__main__":
    print("--- Singleton ---")
    s1 = Settings.get_instance()
    s2 = Settings.get_instance()
    s1.theme = "dark"
    print("Один и тот же объект:", s1 is s2)
    print("Тема через s2:", s2.theme)

    print("\n--- Factory Method ---")
    EmailFactory().notify("Заказ оформлен")
    SmsFactory().notify("Заказ оформлен")

    print("\n--- Abstract Factory ---")
    Room(ModernFactory()).show()
    Room(ClassicFactory()).show()

    print("\n--- Builder ---")
    for builder in (BeefBurgerBuilder(), VeggieBurgerBuilder()):
        BurgerDirector(builder).construct_burger()
        print(builder.get_result())
