from abc import ABC

class Marriage(ABC):
    def person(self):
        pass

    def house(self):
        print("Gifting House")

class girl(Marriage):
    def person(self):
        print("Tom")

g = girl()
g.person()
g.house()