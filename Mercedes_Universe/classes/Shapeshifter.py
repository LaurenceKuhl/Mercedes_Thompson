from classes.Creature import Creature
from collections import namedtuple
from classes.City import City

Pet = namedtuple("Pet", ["name", "specie"])

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