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

    def add_animal(self, animal):
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
        if not animal.can_be_moved():
            raise ValueError("Animal cannot be moved while under treatment.")
        self.animals.remove(animal)
        animal.enclosure = None

    def clean(self):
        self.cleanliness = 100
        return f"{self.name} cleaned."

    def status(self):
        return f"{self.name} | {len(self.animals)}/{self.capacity} clean:{self.cleanliness}%"

