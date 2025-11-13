'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enum import Enum, auto
from datetime import date
from abc import ABC, abstractmethod

class Animal(ABC):
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
        return f"{self.name} eats {self.daily_ration_kg}kg of food."

    def sleep(self):
        return f"{self.name} is resting."

    def can_be_moved(self):
        return not self.health.is_under_treatment()

    @abstractmethod
    def make_sound(self):
        pass

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

class SeverityLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class HealthIssue:
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

