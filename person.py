import random
<<<<<<< HEAD
import pytest
from virus import Virus
# TODO: Import the virus class



class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = None
        self.is_alive = True  # Boolean
        self.is_vaccinated = None  # Boolean
        self.infection = None  # Virus or None

    def did_survive_infection(self):
        random_number = random.randint(0,1)

        if (random_number < self.infection.mortality_rate):
            return False
        else:
            self.is_vaccinated = True
            return True

        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        '''
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''


def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)

    assert person._id == 1
    assert person.is_alive == True
    assert person.is_vaccinated == True
    assert person.infection == False


def test_not_vacc_person_instantiation():
    person = Person(1, False)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    pass


def test_sick_person_instantiation():
    # import the virus class for the testing
    from virus import Virus
    virus = Virus("Dysentery", 0.7, 0.2)

    # TODO: complete your own assert statements that test
    # the values at each attribute
    person = Person(1, False, virus)
    pass
=======
# TODO: Import the virus clase

class Person(object):
    '''
    Person objects will populate the simulation.
    _____Attributes______:
    _id: Int.  A unique ID assigned to each person.
    is_vaccinated: Bool.  Determines whether the person object is vaccinated against
        the disease in the simulation.
    is_alive: Bool. All person objects begin alive (value set to true).  Changed
        to false if person object dies from an infection.
    infection:  None/Virus object.  Set to None for people that are not infected.
        If a person is infected, will instead be set to the virus object the person
        is infected with.
    _____Methods_____:
    __init__(self, _id, is_vaccinated, infected=False):
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding parameter
            passed during instantiation.
        - If person is chosen to be infected for first round of simulation, then
            the object should create a Virus object and set it as the value for
            self.infection.  Otherwise, self.infection should be set to None.
    did_survive_infection(self):
        - Only called if infection attribute is not None.
        - Takes no inputs.
        - Generates a random number between 0 and 1.
        - Compares random number to mortality_rate attribute stored in person's infection
            attribute.
            - If random number is smaller, person has died from disease.
                is_alive is changed to false.
            - If random number is larger, person has survived disease.  Person's
            is_vaccinated attribute is changed to True, and set self.infected to None.
    '''

    def __init__(self, _id, is_vaccinated, infected=None):
        # TODO:  Finish this method.  Follow the instructions in the class documentation
        # to set the corret values for the following attributes.
        self._id = None
        self.is_vaccinated = None
        self.is_alive = None
        self.infected = None


    def did_survive_infection():
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # for resolve_infection.  If person dies, set is_alive to False and return False.
        # If person lives, set is_vaccinated = True, infected = None, return True.  
        pass
>>>>>>> ad38ace30cd3c89e34593b8aebd60867b909f8b0
