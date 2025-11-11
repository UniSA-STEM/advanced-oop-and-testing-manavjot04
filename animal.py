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
    def __init__(self, description, severity):
        self.description = description
        self.severity = severity
        self.reported_on = date.today()
        self.status = "OPEN"

class HealthRecord:
    def __init__(self):
        self.issues = []
