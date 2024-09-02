from typing import List

class City:
    """Defines a city of inhabitants, all of whom are Creatures"""

    def __init__(self, name_city: str) -> None:
        self.name_city = name_city
        self.creatures: List['Creature'] = []  # Forward reference with a string  # noqa: F821

    @property
    def name(self):
        """returns the name of the city"""
        return self.name_city

    def add_inhabitant(self, creature: 'Creature'):  # noqa: F821
        """Adds an inhabitant to the city"""
        self.creatures.append(creature)
        creature.city = self  # Set the city for the creature

    def remove_inhabitant(self, creature: 'Creature'):  # noqa: F821
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
