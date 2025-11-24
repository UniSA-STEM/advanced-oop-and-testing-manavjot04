File: README.md
Description: Zoo Management System – Advanced Programming Assignment Overview
Author: Manavjot Singh Dutta
ID: 110430330
Username: DUTMY005
This is my own work as defined by the University's Academic Integrity Policy.

This project is an object-oriented Zoo Management System implemented in Python as part of the Advanced Programming assignement. The system demonstrates abstraction, encapsulation, inheritance, and polymorphism while modelling real-world zoo operations and the design centres around three core domains: animals, enclosures, and staff.

Animals are represented using an abstract Animal base class with concrete subclasses (Mammal, Reptile, Bird) that override specific behaviours such as make_sound(). Each animal maintains an independent HealthRecord, allowing multiple issues, severity levels, treatment plans, and movement restrictions to be tracked in a structured and realistic way.

Enclosures enforce strict business rules, including species compatibility, environmental matching, capacity limits, and restrictions on moving animals under treatment and the staff members are modelled using inheritance, with Zookeeper and Veterinarian classes supporting feeding, cleaning, diagnosing, and treatment workflows. Assignment-based permissions ensure staff may only interact with animals and enclosures they are responsible for.

Comprehensive automated testing was implemented using pytest. In addition to it, the tests cover enclosure rules, health workflows, movement restrictions, and staff permissions to ensure the system behaves correctly under various scenarios.

This assignment demonstrates strong application of OOP principles, robust error handling, clean code structure, and test-driven development practices.