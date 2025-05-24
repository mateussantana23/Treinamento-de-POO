class Cat:
    def __init__(self, name, age, specie):
        self.name = name
        self.age = age
        self.breed = breed
    def __str__(self):
        return f"{self.name} is {self.age} years old, from {self.breed} breed"
    def speak(self, sound):
        return f"{self.name} says {sound}"
tim=Cat("Tim", 4, "Persa")
print(tim)
