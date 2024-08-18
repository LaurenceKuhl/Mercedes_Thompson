"""
File: test_creature_class.py
Author: Laurence Kuhlburger
Email: laurence.kuhlburger@gmail.com
Github: https://github.com/laurencekuhl
Description: assertions to check for the Creature class
"""
import datetime
import pytest
from mercedes_universe import Creature



@pytest.fixture
def mercy_fixture():
    """Create the character Mercy for testing purposes"""
    return Creature("Mercy", gender = "F", birthday = datetime.datetime(1989, 6, 1))

def test_correctness_of_attributes_(mercy_fixture):
    """Checks the creature function"""
    assert mercy_fixture.name == 'Mercy'
    assert mercy_fixture.gender == "F"
    assert mercy_fixture.birthday == datetime.datetime(1989, 6, 1)
