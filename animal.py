'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enum import Enum, auto

class DietType(Enum):
    HERBIVORE = auto()
    CARNIVORE = auto()
    OMNIVORE = auto()

class EnvironmentType(Enum):
    SAVANNAH = auto()
    AQUATIC = auto()
    RAINFOREST = auto()
    DESERT = auto()
    AVIARY = auto()
    REPTILE_HOUSE = auto()
