import genetics
import random
import string


random.seed("YouAreNotAloneWhenAtWork...")



world = genetics.Population(10)
world.calcFitness("012345")
print world
world.sort("fitness")
print world