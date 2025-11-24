'''
File: enclosure.py
Description: This defines the Enclosure class which houses the animals and enforces
rules such as capacity, species compatibility, and environment.
Author: Manavjot Singh Dutta
ID: 110430330
Username: DUTMY005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import EnvironmentType

class Enclosure:
# This represents a physical enclosure in the zoo.
    def __init__(self, name, species_allowed, environment, capacity):
        self.name = name
        self.species_allowed = species_allowed
        self.environment = environment
        self.capacity = capacity
        self.cleanliness = 100
        self.animals = []

    def add_animal(self, animal):
    # For adding the animal.
        if len(self.animals) >= self.capacity:
            raise ValueError("Enclosure is full.")
        if animal.species != self.species_allowed:
            raise ValueError("Wrong species for this enclosure.")
        if animal.required_environment != self.environment:
            raise ValueError("Environment mismatch.")
        if not animal.can_be_moved():
            raise ValueError("Animal cannot be moved due to treatment.")
        self.animals.append(animal)
        animal.enclosure = self

    def remove_animal(self, animal):
    # For removing the animal.
        if not animal.can_be_moved():
            raise ValueError("Animal cannot be moved while under treatment.")
        self.animals.remove(animal)
        animal.enclosure = None

    def clean(self):
    # For cleaning of the enclosure.
        self.cleanliness = 100
        return f"{self.name} cleaned."

    def status(self):
    # For showing the staus of the enclosure.
        return f"{self.name} | {len(self.animals)}/{self.capacity} clean:{self.cleanliness}%"

