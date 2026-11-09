
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.messages = []
        return cls._instance

    def log(self, text):
        self.messages.append(text)



class Truck:
    def deliver(self):
        return "Грузовик везёт груз по дороге"


class Ship:
    def deliver(self):
        return "Корабль везёт груз по морю"


class Logistics:
    def create_transport(self):
        raise NotImplementedError

    def plan_delivery(self):
        return self.create_transport().deliver()


class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()



class WindowsButton:
    def render(self):
        return "Кнопка Windows"


class WindowsCheckbox:
    def render(self):
        return "Флажок Windows"


class MacButton:
    def render(self):
        return "Кнопка macOS"


class MacCheckbox:
    def render(self):
        return "Флажок macOS"


class WindowsFactory:
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory:
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


def show_interface(factory):
    print(factory.create_button().render())
    print(factory.create_checkbox().render())



class Computer:
    def __init__(self):
        self.parts = []

    def __str__(self):
        return ", ".join(self.parts)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self, name):
        self.computer.parts.append("процессор " + name)

    def add_ram(self, size):
        self.computer.parts.append("память " + size)

    def add_gpu(self, name):
        self.computer.parts.append("видеокарта " + name)

    def get_result(self):
        return self.computer



print("--- Singleton ---")
a = Logger()
b = Logger()
a.log("привет")
print("Это один объект:", a is b)
print("Сообщения через b:", b.messages)

print("\n--- Factory Method ---")
for logistics in (RoadLogistics(), SeaLogistics()):
    print(logistics.plan_delivery())

print("\n--- Abstract Factory ---")
show_interface(WindowsFactory())
show_interface(MacFactory())

print("\n--- Builder ---")
builder = ComputerBuilder()
builder.add_cpu("Intel i5")
builder.add_ram("16 ГБ")
builder.add_gpu("RTX 4070")
print("Компьютер:", builder.get_result())