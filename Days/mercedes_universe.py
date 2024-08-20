"""
File: day_1.py
Author: Laurence Kuhlburger
Email: laurence.kuhlburger@gmail.com
Github: https://github.com/laurencekuhl
Description: day 1 of my new coding habit
"""
from __future__ import annotations

import datetime
from typing import List, Optional
from collections import namedtuple

Pet = namedtuple('Pet', ['name', 'specie'])

class Creature:
    """Creates a Creature which could be a human, werewolf or shapeshifter"""

    def __init__(
        self, name: str, gender: str, birthday: datetime.date, city: City = None
    ) -> None:
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.city = city if city is not None else None

    def __repr__(self) -> str:
        """function printing the creature's name gender and birthday returns string"""
        return f"Creature('{self.name}', {self.gender},  {self.birthday})"

    def speaks(self, lines: str) -> None:
        """function that prints the name of the character and the lines they say"""
        return print(f"{self.name} says '{lines}'")

    @property
    def age(self) -> int:
        """returns the age of the creature"""
        today = datetime.date.today()
        return today.year - self.birthday.year

    def city(self) -> str:
        """returns the city the creature lives in"""
        if self.city:
            return self.city.name
        else:
            return None

class Shapeshifter(Creature):
    """Creates a Shapeshifter which turns into a specific animal"""

    def __init__(self, name, gender, birthday, animal, city: City = None, pet: Pet = None) -> None:
        super().__init__(name, gender, birthday)
        self.animal = animal
        self.human_shape = True
        self.pet = pet

    def __repr__(self):
        """returns the attributes of the shapeshifter"""
        return f"Shapeshifter('{self.name}', {self.gender},  {self.animal})"

    def shapeshift(self) -> None:
        """turns the shapeshifter back into a human or into its animal"""
        if self.human_shape:
            self.human_shape = False
            print(f"{self.name} swiftly turns into a {self.animal}")
        else:
            self.human_shape = True
            print(f"{self.name} swiftly turns back into a human!")
    
    def adopt_pet(self, pet: Pet) -> None:
        """Adopts a pet"""
        self.pet = pet

class Werewolf(Creature):
    """Creates a Werewolf which is either dominant or submissive and has a fur color"""

    def __init__(  # pylint: disable=too-many-arguments
        self, name, gender, birthday: datetime, fur_color = None, dominance: bool = False, pack = None, city: City = None
    ):
        super().__init__(name, gender, birthday)
        self.fur_color = fur_color
        self.dominance = dominance
        self.pack = pack

    def __repr__(self):
        return (
            f"Werewolf(\n"
            f"    '{self.name}',\n"
            f"    {self.gender},\n"
            f"    {self.fur_color},\n"
            f"    dominance: {self.dominance}\n"
            f")"
        )

    def rare(self) -> bool:
        """Returns true if the fur color is rare and false if not"""
        fur = {
            "Pastel": True,
            "Glow": False,
            "Brown": False,
            "Violet": True,
            "Blue Iris": True,
            "White": False,
            "Black": False,
            "Mahogany": False,
        }
        return fur[self.fur_color]

class City:
    """Defines a city of inhabitants, all of whom are Creatures"""

    def __init__(self, name_city: str, position: Position = None) -> None:
        self.name_city = name_city
        self.creatures: List[Creature] = []  # Use forward reference with List[Creature]

    @property
    def name(self):
        return self.name_city

    def add_inhabitant(self, creature: Creature):
        """Adds an inhabitant to the city"""
        self.creatures.append(creature)
        creature.city = self  # Set the city for the creature

    def remove_inhabitant(self, creature: Creature):
        """Removes inhabitant from the city in case they move or pass away"""
        self.creatures.remove(creature)
        creature.city = None  # Set the city for the creature

    def survey_population(self) -> List[str]:
        """Shows a list of different inhabitants of the city"""
        return [f"{creature.name}" for creature in self.creatures]

    @property
    def population_size(self) -> int:
        """returns the size of the population"""
        print(len(self.creatures))
        return len(self.creatures)

if __name__ == "__main__":
    mercy = Shapeshifter("Mercy", "F", datetime.datetime(1989, 6, 1), animal = 'coyote',pet = Pet(name="Meredith", specie="cat"))
    mercy.speaks("Hey everyone")
    print(mercy.city)
    print(repr(mercy))
    atlanta = City('Atlanta')
    adam = Werewolf(
        "Adam", "male", datetime.datetime(1989, 2, 12), "Black", True, atlanta
    )
    adam.speaks("Hi")
    print(adam.age)
    print(mercy.age)
    print(adam.rare())
    atlanta.add_inhabitant(adam)
    print(adam.city.name)
    oliver = Shapeshifter("Oliver", "M", datetime.datetime(1995, 9, 15), "owl")
    oliver.shapeshift()
    atlanta.add_inhabitant(oliver)
    print(atlanta.population_size)

