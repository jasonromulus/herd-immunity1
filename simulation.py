import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    '''
    Main class that will run the herd immunity simulation program.  Expects initialization
    parameters passed as command line arguments when file is run.
    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    _____Attributes______
    logger: Logger object.  The helper object that will be responsible for writing
    all logs to the simulation.
    population_size: Int.  The size of the population for this simulation.
    population: [Person].  A list of person objects representing all people in
        the population.
    next_person_id: Int.  The next available id value for all created person objects.
        Each person should have a unique _id value.
    virus_name: String.  The name of the virus for the simulation.  This will be passed
    to the Virus object upon instantiation.
    mortality_rate: Float between 0 and 1.  This will be passed
    to the Virus object upon instantiation.
    basic_repro_num: Float between 0 and 1.   This will be passed
    to the Virus object upon instantiation.
    vacc_percentage: Float between 0 and 1.  Represents the total percentage of population
        vaccinated for the given simulation.
    current_infected: Int.  The number of currently people in the population currently
        infected with the disease in the simulation.
    total_infected: Int.  The running total of people that have been infected since the
    simulation began, including any people currently infected.
    total_dead: Int.  The number of people that have died as a result of the infection
        during this simulation.  Starts at zero.
    _____Methods_____
    __init__(population_size, vacc_percentage, virus_name, mortality_rate,
     basic_repro_num, initial_infected=1):
        -- All arguments will be passed as command-line arguments when the file is run.
        -- After setting values for attributes, calls self._create_population() in order
            to create the population array that will be used for this simulation.
    _create_population(self, initial_infected):
        -- Expects initial_infected as an Int.
        -- Should be called only once, at the end of the __init__ method.
        -- Stores all newly created Person objects in a local variable, population.
        -- Creates all infected person objects first.  Each time a new one is created,
            increments infected_count variable by 1.
        -- Once all infected person objects are created, begins creating healthy
            person objects.  To decide if a person is vaccinated or not, generates
            a random number between 0 and 1.  If that number is smaller than
            self.vacc_percentage, new person object will be created with is_vaccinated
            set to True.  Otherwise, is_vaccinated will be set to False.
        -- Once len(population) is the same as self.population_size, returns population.
    '''

    def __init__(self, pop_size, vacc_percentage, initial_infected=1, virus=None):
        self.logger = Logger("interactions.txt")
        self.population = list()  # List of Person objects
        self.pop_size = pop_size  # Int
        self.next_person_id = 0
        self.virus = virus
        self.initial_infected = initial_infected  # Int
        # FIXME: Use the variables below
        self.total_infected = 0
        self.current_infected = 0
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.newly_infected = []
        self.population = self._create_population(initial_infected)
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.

    def _create_population(self, initial_infected):
        infected_count = 0

        while len(self.population) < self.pop_size:
            id = len(self.population) + 1
            if infected_count < self.initial_infected:

                new_person = Person(id, True, virus)
                self.total_infected += 1
                infected_count +=1
                self.population.append(new_person)
            else:
                if random.random() > self.vacc_percentage:
                    new_person = Person(id, False, virus)
                    self.population.append(new_person)
                else:
                    new_person = Person(id, True, virus)
                    self.population.append(new_person)

        # return self.population
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people)
        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.
        # This method should be a loop and go all the way up to the self.pop_size and randomly assign characteristics to the people we create like vaccinated_option = random.choice(True,False)

    def _simulation_should_continue(self):
        while self.pop_size > 0 or not self.vacc_percentage == 1:
            return True
        else:
            return False

    def run(self):
        self._create_population(initial_infected)
        should_continue = self._simulation_should_continue()
        time_step_counter = 0
        while should_continue == True:
            self.time_step()
            time_step_counter += 1
            should_continue = self._simulation_should_continue()

        print("The simulation has ended after", step_counter, " turns.")
        print("Total infected", self.total_infected, "Total Dead", self.total_dead)
        print("Interactions where indvidual as safe from vacciation", self.vacc_int)


    def choose_infected(self):
        return random.choice(self.newly_infected)

    # Test later today in an index.py file
    def time_step(self):
        total_interactions = 0
        # calling get_random_person method to randomly choose person from total population
        rand_person = random.choice(self.population)
        # looping through population to find infected person
        for person in self.population:
            if person.infection == virus:
                # creates loop for sick person to interact with 100 randos
                while total_interactions <= 100:
                    # checking if rando is alive and calling interaction method
                    if rand_person.is_alive:
                        self.interaction(person, rand_person)
                        total_interactions += 1
                    else:
                        # if they're dead the method starts over
                        self.time_step()

    def append_newly_infected(self, random_person):
        if random_person.is_vaccinated() == False:
            num = random.randint(0, 1)
            if num < self.virus.repro_rate:
                self.newly_infected.append(random_person._id)
                random_person.infection = virus

    def interaction(self, person, random_person):
        # Assert statements are to check if
        assert person.is_alive == True
        assert random_person.is_alive == True

        # '''This method should be called any time two living people are selected for an
        # interaction. It assumes that only living people are passed in as parameters.

        # Args:
        #     person1 (person): The initial infected person
        #     random_person (person): The person that person1 interacts with.
        # '''
        # self.logger.log_interaction(person, random_person)
        # self.append_newly_infected(person, random_person)

        # # TODO: Finish this method.d
        # #     attribute can be changed to True at the end of the time step.
        # # TODO: Call logger method during this method.
        # pass
        if person.infection == virus and random_person.infection == virus:
            self.logger.log_interaction(person, random_person)
        elif person.infection == virus and random_person.is_vaccinated == True:
            self.logger.log_interaction(person, random_person)
        elif person.infection == virus and random_person.is_vaccinated == False:
            self.logger.log_interaction(person, random_person)
        else:
            pass

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = list()


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])

    virus = Virus(virus_name, basic_repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
