"""
File: day_1.py
Author: Laurence Kuhlburger
Email: laurence.kuhlburger@gmail.com
Github: https://github.com/laurencekuhl
Description: day 1 of my new coding habit
"""

import datetime
from abc import ABC
from typing import Any

import click


class Creature:
    """Creates a Creature which could be a human, werewolf or shapeshifter"""

    def __init__(self, name: str, gender: str, birthday: datetime.date) -> None:
        self.name = name
        self.gender = gender
        self.birthday = birthday

    def __repr__(self):
        return f"Creature('{self.name}', {self.gender},  {self.birthday})"

    def speaks(self, lines: str) -> None:
        return print(f"{self.name} says '{lines}'")


class Shapeshifter(Creature):
    def __init__(self, name, gender, birthday, animal) -> None:
        super().__init__(name, gender, birthday)
        self.animal = animal
        self.human_shape = True

    def __repr__(self):
        return f"Shapeshifter('{self.name}', {self.gender},  {self.animal})"

    def shapeshift(self) -> None:
        if self.human_shape:
            self.human_shape = False
            print(f"{self.name} swiftly turns into a {self.animal}")
        else:
            self.human_shape = True
            print(f"{self.name} swiftly turns back into a human!")


class Werewolf(Creature):
    def __init__(
        self, name, gender, birthday: datetime, fur_color, dominance: bool, pack
    ):
        super().__init__(name, gender, birthday)
        self.fur_color = fur_color
        self.dominance = dominance
        self.pack = pack

    def __repr__(self):
        return f"Werewolf('{self.name}', {self.gender},  {self.fur_color})"

    def rare(self) -> bool:
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
    def __init__(
        self,
        name: str,
        gender: str,
        birthday: datetime,
        fur_color,
        dominance: bool,
        pack,
    ):
        pass


# @click.command()
# @click.option('-p', '--p', help='Specify which character to create')

if __name__ == "__main__":
    mercy = Creature("Mercy", "F", datetime.datetime(1989, 6, 1))
    mercy.speaks("Hey everyone")
    print(repr(mercy))
    adam = Werewolf(
        "Adam", "male", datetime.datetime(1989, 2, 12), "Black", True, "Tri-cities"
    )
    adam.speaks("Hi")
    print(adam.rare())
