class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Cat(Animal):
    def __init__(self, name, weight, likesWool):
        super().__init__(name, weight)
        self.likesWool = likesWool
    def meow():
        print('Meow!')
    def introduce(self):
        wool = "do not like"
        if (self.likesWool):
              wool = "like"
        print('Hello, I am a cat named ' + self.name + '. I weigh ' + str(self.weight) + ' kg and ' + wool + ' wool.')

class Dog(Animal):
    def __init__(self, name, weight, collarLength):
        super().__init__(name, weight)
        self.collarLength = collarLength
    def bark():
        print('Croff! Croff!')
    def introduce(self):
        print('Hello, I am a dog named ' + self.name + '. I weigh ' + str(self.weight) + ' kg and my collar is ' + str(self.collarLength) + ' cm long.')

class Shark(Animal):
    def __init__(self, name, weight, eatenSurfers, isHungry):
        super().__init__(name, weight)
        self.eatenSurfers = eatenSurfers
        self.isHungry = isHungry
    def swim():
        print('Splash!')
    def introduce(self):
        hungry = "not hungry"
        if(self.isHungry):
            hungry = "hungry"
        print('Hello, I am a shark named ' + self.name + '. I weigh ' + str(self.weight) + ' kg and at the moment I am ' + hungry + '. I already ate ' + str(self.eatenSurfers) + ' surfers!')


Cat("Kitty", 5.3, True).introduce()
Cat("Kretze", 4.567, False).introduce()

Dog("Fenris", 15.33, 30.0).introduce()
Dog("Basker", 20.45, 34.0).introduce()

Shark("Whitey", 1217.459, 217, True).introduce()
Shark("Clarence", 1098.614, 2, False).introduce()
