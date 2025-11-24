'''
File: animal.py
Description: Defines the animal hierarchy and health system for the zoo which includes
animal types, diet/environment enums, and health records.
Author: Manavjot Singh Dutta
ID: 110430330
Username: DUTMY005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enum import Enum, auto
from datetime import date
from abc import ABC, abstractmethod

class Animal(ABC):
# This represents the animal in the zoo.
    def __init__(self, name, species, age, diet, daily_ration_kg, required_environment):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet
        self.daily_ration_kg = daily_ration_kg
        self.required_environment = required_environment
        self.health = HealthRecord()
        self.enclosure = None

    def eat(self):
    # This shows the animal's eating.
        return f"{self.name} eats {self.daily_ration_kg}kg of food."

    def sleep(self):
    # This shows the animal status whether it is sleeping or not.
        return f"{self.name} is resting."

    def can_be_moved(self):
    # This shows whether it shall be moved or not.
        return not self.health.is_under_treatment()

    @abstractmethod
    def make_sound(self):
    # This for its sound 
        pass

class DietType(Enum):
# This shows what type of food it eats.
    HERBIVORE = auto()
    CARNIVORE = auto()
    OMNIVORE = auto()

class EnvironmentType(Enum):
# This shows the environement it needs to live in.
    SAVANNAH = auto()
    AQUATIC = auto()
    RAINFOREST = auto()
    DESERT = auto()
    AVIARY = auto()
    REPTILE_HOUSE = auto()

class SeverityLevel(Enum):
# This shows how much serious the issue is.
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class HealthIssue:
# This shows the single health issue for an animal.
    def __init__(self, description, severity, treatment_plan=""):
        self.description = description
        self.severity = severity
        self.reported_on = date.today()
        self.treatment_plan = treatment_plan
        self.status = "OPEN"
        self.notes = []

    def start_treatment(self, plan):
        self.treatment_plan = plan
        self.status = "TREATMENT"

    def close(self, note=""):
        if note:
            self.notes.append(note)
        self.status = "CLOSED"

class HealthRecord:
# This shows all the health issues for a single animal.
    def __init__(self):
        self.issues = []

    def open_issue(self, description, severity):
        new_issue = HealthIssue(description, severity)
        self.issues.append(new_issue)
        return new_issue

    def active_issues(self):
        return [i for i in self.issues if i.status != "CLOSED"]

    def is_under_treatment(self):
        return any(i.status == "TREATMENT" for i in self.issues)

class Mammal(Animal):
# Subclass of the animal
    def make_sound(self):
        return f"{self.name} roars."

class Reptile(Animal):
# Subclass of the animal
    def make_sound(self):
        return f"{self.name} hisses."

class Bird(Animal):
# Subclass of the animal
    def make_sound(self):
        return f"{self.name} chirps."

