from classes.Creature import Creature
from classes.Power import Power

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
