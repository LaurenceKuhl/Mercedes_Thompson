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
import pathlib
from dataclasses import dataclass
#local imports
from classes.City import City
from classes.Shapeshifter import Shapeshifter
from classes.Werewolf import Werewolf
from classes.Vampire import Vampire
from classes.Power import Power


if __name__ == "__main__":
    Pet = namedtuple("Pet", ["name", "specie"])
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
