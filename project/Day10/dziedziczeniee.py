#dziedziczenie

class Parent(object):
    def __init__(self):
        print("Parent init")
    def parent(self):
        print("Parent parent")
    def poke(self):
        print("Parent poke")

class Child(Parent):
    def __init__(self):
        super().__init__() #wywolanie glownej fukcnji przez super
        print("Child init")
    def poke(self):
        print("Child poke")

class Client(Parent):
    def __init__(self):
        super().__init__()
        self.order = "cos"

parent = Parent()
parent.parent()
parent.poke()

print("------")

child = Child()
child.poke()
child.parent()

