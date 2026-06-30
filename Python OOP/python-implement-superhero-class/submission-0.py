class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health

superhero = SuperHero("Batman", "Intelligence", "100")
superhero2 = SuperHero("Superman", "Strength", "150")



print(superhero.name)
print(superhero.power) 
print(superhero.health) 
print(superhero2.name)
print(superhero2.power) 
print(superhero2.health) 
