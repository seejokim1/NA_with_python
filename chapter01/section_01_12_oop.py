# =========================================================
# Section (1.12) 객체지향 프로그래밍(OOP)
# =========================================================

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print(self.name, "barks")

dog = Dog("Buddy")
dog.speak()
