"""
File: test_creature_class.py
Author: Laurence Kuhlburger
Email: laurence.kuhlburger@gmail.com
Github: https://github.com/laurencekuhl
Description: assertions to check for the Creature class
"""
import datetime
import os
import pytest
from classes.Creature import Creature



project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
letter_path = os.path.join(project_root, 'Letters', 'letter.txt')


@pytest.fixture
def mercy_fixture():
    """Create the character Mercy for testing purposes"""
    return Creature("Mercy", gender="F", birthday=datetime.datetime(1989, 6, 1))

def test_correctness_of_attributes_(mercy_fixture):
    """Checks the creature function"""
    assert mercy_fixture.name == "Mercy"
    assert mercy_fixture.gender == "F"
    assert mercy_fixture.birthday == datetime.datetime(1989, 6, 1)

def test_read_letter_(mercy_fixture):
    """Checks the creature function"""
    assert mercy_fixture.reads_letter(letter_path) == None