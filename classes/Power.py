from dataclasses import dataclass

@dataclass
class Power:
    """Creates a power that a Vampire can have"""
    power_name: str
    power_strength: int

    def powerful(self) -> bool:
        """Returns true if the power is strong and false if not"""
        return self.power_strength > 5