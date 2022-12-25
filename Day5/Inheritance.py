class animal:

    def eat(self):
        print("Animal Eat method")

class Dog(animal):
    def bark(self):
        print("Dog bark method")

d = Dog()
d.bark()
d.eat()


class Google:
    def loginPage(self):
        print("Login Page")

    def HomePage(self):
        print("Home Page")


class YouTube(Google):
    def HomePage(self):
        print("Youtbe Home Page")

y = YouTube()
y.HomePage()
y.loginPage()