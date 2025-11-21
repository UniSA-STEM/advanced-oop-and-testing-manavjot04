'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import SeverityLevel

class StaffMember:
    def __init__(self, name):
        self.name = name
        self.assigned_animals = set()
        self.assigned_enclosures = set()

    def assign_animal(self, animal):
        self.assigned_animals.add(animal)

    def assign_enclosure(self, enclosure):
        self.assigned_enclosures.add(enclosure)


class Zookeeper(StaffMember):
    def feed(self, animal):
        if animal not in self.assigned_animals:
            raise PermissionError("Not assigned to this animal.")
        return f"{self.name} feeds {animal.name}. {animal.eat()}"

    def clean_enclosure(self, enclosure):
        if enclosure not in self.assigned_enclosures:
            raise PermissionError("Not assigned to this enclosure.")
        return enclosure.clean()
    

class Veterinarian(StaffMember):
    def health_check(self, animal, note="Healthy"):
        if animal not in self.assigned_animals:
            raise PermissionError("Not assigned to this animal.")
        return f"{self.name} checks {animal.name}: {note}"

    def diagnose(self, animal, description, severity, plan):
        issue = animal.health.open_issue(description, severity)
        issue.start_treatment(plan)
        return f"{self.name} diagnosed {animal.name} and started treatment."

    def discharge(self, animal, note="Recovered"):
        for issue in animal.health.active_issues():
            issue.close(note)
        return f"{animal.name} has recovered."
