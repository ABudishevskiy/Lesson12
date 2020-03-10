# Создайте класс который будет хранить параметры для подключения к физическому юниту(например switch).
# В своем списке атрибутов он должен иметь минимальный набор (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и сеттеров(@property).
# У вас должна быть возможность получения и назначения этих атрибутов в классе
class Switch():
    def __init__(self):
        self.unit_name = None
        self.mac_address = None
        self.ip_address = None
        self.login = None
        self.password = None

    # x = property()

    @property
    def x(self):
        return self.password
    @property
    def y(self, value):
        return self.login
    @property
    def i(self, value):
        return self.ip_address
    @property
    def m(self, value):
        return self.mac_address
    @property
    def u(self, value):
        return self.unit_name

    @x.setter
    def x(self, value):
        self.password = value
    def y(self, value):
        self.login = value
    def i(self, value):
        self.ip_address = value
    def m(self, value):
        self.mac_address = value
    def u(self, value):
        self.unit_name = value

a = Switch()
a.x = 7
a.y = 9


print(a.y)