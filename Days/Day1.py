"""
File: day_1.py
Author: Laurence Kuhlburger
Email: laurence.kuhlburger@gmail.com
Github: https://github.com/laurencekuhl
Description: day 1 of my new coding habit
"""

import datetime

class Inhabitant:
    def __init__(self, name: str, gender: str, birthday: datetime.date) -> None:
        self.name = name
        self.gender = gender
        self.birthday = birthday

    def speaks(self, lines: str) -> None:
        return print(f"{self.name} says '{lines}'")
    
class Werewolf(Inhabitant):
    def __init__(self, name, gender, birthday, fur_color, dominance: bool, pack):
        super().__init__(name, gender, birthday)
        self.fur_color = fur_color
        self.dominance = dominance
        self.pack = pack


mercy = Inhabitant("Mercy","F",datetime.datetime(1989, 6, 1))
mercy.speaks("Hey everyone")
adam = Werewolf("Adam", "male", datetime.datetime(1989, 2, 12), 'Grey', True, 'Tri-cities')
adam.speaks("Hi")