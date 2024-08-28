from classes.City import City
from datetime import datetime
import pathlib

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
