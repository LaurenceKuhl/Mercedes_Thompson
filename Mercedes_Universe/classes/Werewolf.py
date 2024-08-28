from datetime import datetime
from classes.Creature import Creature
from classes.City import City

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