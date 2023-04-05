class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat(self.pet_food)
    def bathe(self):
        self.pet.noise("Splash! Splash! I'm clean now.")


class Pet:
    def __init__(self,name,type_of_pet,tricks,health=100,energy=100):
        self.name = name
        self.type_of_pet = type_of_pet
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
    def eat(self,food):
        self.energy += 5
        self.health += 10
        print(f"{self.name} eats {food} and gains 5 energy and 10 health.")
    def play(self):
        self.health += 5
        self.energy -= 10
    def noise(self, sound):
        print(f"{self.name} says {sound}")

pet1 = Pet("Max", "dog", ["sit", "roll over"])
ninja1 = Ninja("John", "Doe", ["bones", "meat"], "dog food", pet1)

ninja1.feed()
ninja1.walk()
ninja1.bathe()

class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "cat", tricks)
        self.hairball_count = 0
        
    def cough_up_hairball(self):
        self.hairball_count += 1
        self.health -= 5
        print(f"{self.name} coughs up a hairball and loses 5 health.")

cat = Cat("Whiskers", ["purr", "scratch"])
cat.sleep()
cat.play()
cat.eat("cat food")
cat.noise("Meow!")
cat.cough_up_hairball()