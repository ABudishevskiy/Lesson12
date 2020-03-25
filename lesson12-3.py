# Создайте класс который будет хранить параметры для подключения к физическому юниту(например switch).
# В своем списке атрибутов он должен иметь минимальный набор (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и сеттеров(@property).
# У вас должна быть возможность получения и назначения этих атрибутов в классе
class Switch():

    def __init__(self):
        self._unit_name = None
        self._mac_address = None
        self._ip_address = None
        self._login = None
        self._password = None


    @property
    def password(self):
        return self.password
    @property
    def login(self):
        return self._login
    @property
    def ip_address(self):
        return self._ip_address
    @property
    def mac_address(self):
        return self._mac_address
    @property
    def unit_name(self):
        return self._unit_name

    @password.setter
    def password(self, value):
        self._password = value

    @login.setter
    def login(self, value):
        self._login = value

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value

a = Switch()
a.password = 7
a.login = 9


print(a.login)