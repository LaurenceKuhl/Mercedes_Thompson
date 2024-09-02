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
from mercedes_universe import Vampire

@pytest.fixture
def marsilia_fixture():
    """Create the character Marsilia for testing purposes"""
    return Vampire("Marsilia", "F", datetime.datetime(1989, 6, 1))