"""
File: day_1.py
Author: Laurence Kuhlburger
Email: laurence.kuhlburger@gmail.com
Github: https://github.com/laurencekuhl
Description: day 1 of my new coding habit
"""

import datetime


class Creature:
    """Creates a Creature which could be a human, werewolf or shapeshifter"""

    def __init__(self, name: str, gender: str, birthday: datetime.date) -> None:
        self.name = name
        self.gender = gender
        self.birthday = birthday

    def __repr__(self) -> str:
        """function printing the creature's name gender and birthday returns string"""
        return f"Creature('{self.name}', {self.gender},  {self.birthday})"

    def speaks(self, lines: str) -> None:
        """function that prints the name of the character and the lines they say"""
        return print(f"{self.name} says '{lines}'")


class Shapeshifter(Creature):
    """Creates a Shapeshifter which turns into a specific animal"""

    def __init__(self, name, gender, birthday, animal) -> None:
        super().__init__(name, gender, birthday)
        self.animal = animal
        self.human_shape = True

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


class Werewolf(Creature):
    """Creates a Werewolf which is either dominant or submissive and has a fur color"""

    def __init__(  # pylint: disable=too-many-arguments
        self, name, gender, birthday: datetime, fur_color, dominance: bool, pack
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


class City:  # pylint: disable=too-few-public-methods
    """STILL under construction"""

    def __init__(  # pylint: disable=too-many-arguments
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
