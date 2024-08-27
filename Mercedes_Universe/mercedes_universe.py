"""
File: mercedes_universe.py
Author: Laurence Kuhlburger
Email: laurence.kuhlburger@gmail.com
Github: https://github.com/laurencekuhl
Description: day 1 of my new coding habit
"""
from __future__ import annotations

import datetime
from collections import namedtuple
from typing import List
import pathlib
from dataclasses import dataclass
from typing import List

Pet = namedtuple("Pet", ["name", "specie"])

class Creature:
    """Creates a creature with a name"""

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

    def get_city_name(self) -> str:
        """returns the city the creature lives in"""
        if self.city:
            return self.city.name
        return "No city"
    
    def move(self, new_city:City) -> None:
        """Moves the creature to a new city"""
        if new_city:
            self.city = new_city
            new_city.add_inhabitant(self)
            print(f"{self.name} has moved to {new_city.name}")
        else:
            self.city.remove_inhabitant(self)

    def reads_letter(self, letter, diagonally=False) -> None:
        """Reads and prints lines from a letter (file). 
        If diagonally=True, prints every other line."""

        file_path = pathlib.Path(letter)

        with file_path.open('r') as file:
            for line_number, line in enumerate(file):
                # Print every line if diagonally is False
                # Print only every other line if diagonally is True
                if not diagonally or line_number % 2 == 0:
                    print(line, end='')  # Use end='' to avoid double newlines

class Shapeshifter(Creature):
    """Creates a Shapeshifter which turns into a specific animal"""

    def __init__( # pylint: disable=too-many-arguments
        self, name, gender, birthday, animal, city: City = None, pet: Pet = None # pylint: disable=too-many-arguments
    ) -> None: # pylint: disable=too-many-arguments
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
@dataclass
class Power:
    """Creates a power that a Vampire can have"""
    power_name: str
    power_strength: int

    def powerful(self) -> bool:
        """Returns true if the power is strong and false if not"""
        return self.power_strength > 5
class Vampire(Creature):
    """Creates a Vampire which is immortal and has a specific blood type"""

    def __init__(self, name, gender, birthday, power: Power = None):
        super().__init__(name, gender, birthday)
        self.name = name
        self.immortal = True
        self.blood_type = "AB"
        self.power = power

    def __repr__(self):
        return (
            f"Vampire(\n"
            f"    '{self.name}',\n"
            f"    {self.gender},\n"
            f"    {self.immortal},\n"
            f")"
        )

class Werewolf(Creature):
    """Creates a Werewolf which is either dominant or submissive and has a fur color"""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        name,
        gender,
        birthday: datetime,
        fur_color=None,
        dominance: bool = False,
        pack=None,
        city: City = None,
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

    def __init__(self, name_city: str) -> None:
        self.name_city = name_city
        self.creatures: List[Creature] = []  # Use forward reference with List[Creature]

    @property
    def name(self):
        """returns the name of the city"""
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
    mercy = Shapeshifter("Mercy", "F", datetime.datetime(1989, 6, 1),
                        animal = 'coyote',pet = Pet(name="Meredith", specie="cat")) #line-too-long
    mercy.speaks("Hey everyone")
    print(mercy.city)
    print(repr(mercy))
    atlanta = City('Atlanta')
    georgia = City('Georgia')
    adam = Werewolf(
        "Adam", "male", datetime.datetime(1989, 2, 12), "Black", True, atlanta
    )
    adam.speaks("Hi")
    print(adam.age)
    print(mercy.age)
    print(adam.rare())
    oliver = Shapeshifter("Oliver", "M", datetime.datetime(1995, 9, 15), "owl")
    oliver.shapeshift()
    atlanta.add_inhabitant(oliver)
    print(atlanta.population_size)
    atlanta.add_inhabitant(adam)
    print(adam.city.name)
    adam.move(georgia)
    print(adam.city.name)
    marsilia = Vampire("Marsilia", "F", 
                    datetime.datetime(1989, 6, 1), power=Power("Teleportation", 10)) 
    print(marsilia.power.powerful())
    print(marsilia.power)