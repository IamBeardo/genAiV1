import genetics
import random

import debug




#random.seed("YouAreNotAloneWhenAtWork...")



world = genetics.Population(100)
#print "World INIT", world
world.calcFitness("0123456789")
world.sort("fitness")
print "world after sort", world

for i in range(100):
    world.generateNewGeneration(fromCopy=False )
    print world.fitness()
    world.mutate(world.nextGeneration,0.20)
    world.setPopulationToNext()
    world.calcFitness("0123456789")
    world.sort("fitness")
    print world.fitness()
    if world.min==0:
        print "Ending, target reached"
        print world
        break



#print world.getAnsastors(world.individuals[0])