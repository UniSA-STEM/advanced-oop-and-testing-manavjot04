'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Mammal, Reptile, Bird, DietType, EnvironmentType, SeverityLevel
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

def main():
    lion_enclosure = Enclosure("Savannah Exhibit", "Lion", EnvironmentType.SAVANNAH, 3)
    simba = Mammal("Simba", "Lion", 5, DietType.CARNIVORE, 8, EnvironmentType.SAVANNAH)
    lion_enclosure.add_animal(simba)

    keeper = Zookeeper("Ava")
    keeper.assign_animal(simba)
    keeper.assign_enclosure(lion_enclosure)

    vet = Veterinarian("Dr. Leo")
    vet.assign_animal(simba)

    print(keeper.feed(simba))
    print(vet.diagnose(simba, "Leg sprain", SeverityLevel.MEDIUM, "Rest"))
    print(vet.discharge(simba))
    print(lion_enclosure.status())

if __name__ == "__main__":
    main()
