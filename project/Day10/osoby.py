class Person():

    def __init__(self, name):
        self.name = name
        self.surname = "Star"
        self.age = "25"

class Employee(Person):

    def __init__(self, position):
        super().__init__("Tomek")
        self.position = position
        self.specjalization = "Python"


class Client(Person):

    def __init__(self, name):
        super().__init__(name)
        self.order = "kalosze"



pracownik = Employee("Programer")
print(pracownik.name)
print(pracownik.position)

print("=-------")

pracownik2 = Employee("Designer")
print(pracownik2.name)
print(pracownik2.position)

print("=-------")

klient = Client("Wanda")
print(klient.name)
print(klient.order)

klient2 = Client("Karola")
print(klient2.name)
print(klient2.order)