'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import EnvironmentType

class Enclosure:
    def __init__(self, name, species_allowed, environment, capacity):
        self.name = name
        self.species_allowed = species_allowed
        self.environment = environment
        self.capacity = capacity
        self.cleanliness = 100
        self.animals = []
