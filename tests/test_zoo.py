'''
File: test_zoo.py
Description: This validates the core functionality of the Zoo Management System, ensuring enclosure logic, 
animal movement rules, health management and the staff permissions operate correctly.
Author: Manavjot Singh Dutta
ID: 110430330
Username: DUTMY005
This is my own work as defined by the University's Academic Integrity Policy.
'''

import sys
import os

# This allows the imports from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

import pytest
from animal import Mammal, Reptile, Bird, DietType, EnvironmentType, SeverityLevel
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian


@pytest.fixture
def setup_zoo():
# Test fixture used to initialise a clean zoo state before each test.
    lion_enc = Enclosure("Savannah", "Lion", EnvironmentType.SAVANNAH, 2)
    reptile_enc = Enclosure("Reptile House", "Python", EnvironmentType.REPTILE_HOUSE, 1)

    simba = Mammal("Simba", "Lion", 5, DietType.CARNIVORE, 8, EnvironmentType.SAVANNAH)
    sly = Reptile("Sly", "Python", 2, DietType.CARNIVORE, 0.5, EnvironmentType.REPTILE_HOUSE)

    keeper = Zookeeper("Ava")
    vet = Veterinarian("Dr. Leo")

    keeper.assign_animal(simba)
    keeper.assign_enclosure(lion_enc)
    vet.assign_animal(simba)

    return lion_enc, reptile_enc, simba, sly, keeper, vet


def test_correct_enclosure_assignment(setup_zoo):
# To test if the animals can be added to the correct enclosure.
    lion_enc, _, simba, _, _, _ = setup_zoo
    lion_enc.add_animal(simba)
    assert simba in lion_enc.animals


def test_species_violation(setup_zoo):
# To test that the enclosure should reject wrong species.
    lion_enc, _, _, sly, _, _ = setup_zoo
    with pytest.raises(ValueError):
        lion_enc.add_animal(sly)


def test_environment_violation(setup_zoo):
# To test that enclosure should reject animals with incompatible environment needs.
    lion_enc, _, _, _, _, _ = setup_zoo
    peng = Bird("Pebbles", "Penguin", 3, DietType.CARNIVORE, 1.2, EnvironmentType.AVIARY)

    with pytest.raises(ValueError):
        lion_enc.add_animal(peng)


def test_capacity_limits(setup_zoo):
# To test that enclosure capacity must not be exceeded.
    lion_enc, _, simba, _, _, _ = setup_zoo
    lion_enc.add_animal(simba)

    nala = Mammal("Nala", "Lion", 4, DietType.CARNIVORE, 7, EnvironmentType.SAVANNAH)
    lion_enc.add_animal(nala)

    scar = Mammal("Scar", "Lion", 6, DietType.CARNIVORE, 10, EnvironmentType.SAVANNAH)

    with pytest.raises(ValueError):
        lion_enc.add_animal(scar)


def test_keeper_feeding(setup_zoo):
# To test the Zookeeper can feed assigned animals only.         
    lion_enc, _, simba, _, keeper, _ = setup_zoo
    lion_enc.add_animal(simba)
    message = keeper.feed(simba)

    assert "feeds Simba" in message


def test_vet_starts_treatment(setup_zoo):
# To test that veterinarian can diagnose issues and put animals into Treatment state.
    lion_enc, _, simba, _, _, vet = setup_zoo
    lion_enc.add_animal(simba)

    vet.diagnose(simba, "Injury", SeverityLevel.MEDIUM, "Rest")

    active = simba.health.active_issues()
    assert active[0].status == "TREATMENT"


def test_movement_blocked_during_treatment(setup_zoo):
# To test that animals under treatment cannot be moved out of an enclosure.
    lion_enc, _, simba, _, _, vet = setup_zoo
    lion_enc.add_animal(simba)

    vet.diagnose(simba, "Injury", SeverityLevel.MEDIUM, "Rest")

    with pytest.raises(ValueError):
        lion_enc.remove_animal(simba)


def test_discharge_closes_issues(setup_zoo):
# To test that after discharge, all active treatment issues should be closed.
    lion_enc, _, simba, _, _, vet = setup_zoo
    lion_enc.add_animal(simba)

    vet.diagnose(simba, "Injury", SeverityLevel.MEDIUM, "Rest")
    vet.discharge(simba)

    active = simba.health.active_issues()
    assert len(active) == 0
