"""
File: test_werewolf_class.py
Author: Laurence Kuhlburger
Email: laurence.kuhlburger@gmail.com
Github: https://github.com/laurencekuhl
Description: assertions to check for the Werewolf class
"""
import datetime

import pytest
from mercedes_universe import Creature

@pytest.fixture
def adam_fixture():
    """Create the character Adam for testing purposes"""
    return Creature("Adam", gender="M", birthday=datetime.datetime(1989, 12, 1),
                    fur_color = "Brown", dominance = True, pack = "Alpha")

def test_correctness_of_attributes_(adam_fixture: Creature):
    """Checks the werewolf function"""
    assert adam_fixture.name == "Adam"
    assert adam_fixture.gender == "M"
    assert adam_fixture.birthday == datetime.datetime(1989, 12, 1)
    assert adam_fixture.age == 31
    assert adam_fixture.dominance
    assert adam_fixture.pack == "Alpha"
    assert adam_fixture.fur_color == "Brown"

def test_rare(adam_fixture: Creature):
    """Checks the rare function"""
    assert not adam_fixture.rare() 