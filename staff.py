'''
File: staff.py
Description: This defines the staff roles (generic staff, zookeepers and veterinarians)
and their responsibilities within the zoo management system.
Author: Manavjot Singh Dutta
ID: 110430330
Username: DUTMY005
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import SeverityLevel

class StaffMember:
    # This is the base class for the staff members.
    def __init__(self, name):
        self.name = name
        self.assigned_animals = set()
        self.assigned_enclosures = set()

    def assign_animal(self, animal):
        # Assigns the animals.
        self.assigned_animals.add(animal)

    def assign_enclosure(self, enclosure):
        # Assigns the enclosure.
        self.assigned_enclosures.add(enclosure)


class Zookeeper(StaffMember):
    # This for the ZooKeeper which is a sort of staffMember only.
    def feed(self, animal):
        if animal not in self.assigned_animals:
            raise PermissionError("Not assigned to this animal.")
        return f"{self.name} feeds {animal.name}. {animal.eat()}"

    def clean_enclosure(self, enclosure):
    # This for the cleaning of an assigned enclosure.
        if enclosure not in self.assigned_enclosures:
            raise PermissionError("Not assigned to this enclosure.")
        return enclosure.clean()
    

class Veterinarian(StaffMember):
    # Staff member responsible for the animal health.
    def health_check(self, animal, note="Healthy"):
        # To get the check of an animal.
        if animal not in self.assigned_animals:
            raise PermissionError("Not assigned to this animal.")
        return f"{self.name} checks {animal.name}: {note}"

    def diagnose(self, animal, description, severity, plan):
        # To diagnose the issue if any.
        issue = animal.health.open_issue(description, severity)
        issue.start_treatment(plan)
        return f"{self.name} diagnosed {animal.name} and started treatment."

    def discharge(self, animal, note="Recovered"):
        # To mark all the issues of the animal as closed.
        for issue in animal.health.active_issues():
            issue.close(note)
        return f"{animal.name} has recovered."
