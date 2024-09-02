from dataclasses import dataclass

@dataclass
class Power:
    """Creates a power that a Vampire can have"""
    power_name: str
    power_strength: int

    def powerful(self) -> bool:
        """Returns true if the power is strong and false if not"""
        return self.power_strength > 5
    
    def __repr__(self) -> str:
        return f"Power('{self.power_name}', {self.power_strength})"
    
    def rare(self)  -> bool:
        """Returns true if the power is rare and false if not"""
        power_sets = {
            'Rare': [
                'Teleportation',
                'Mind Reading',
                'Super Strength',
                'Invisibility'
            ],
            'Common': [
                'Telekinesis',
                'Healing',
                'Flight',
                'Super Speed',
                'Fire Manipulation',
                'Water Manipulation'
            ]}
        
        return self.power_name in power_sets['Rare']

