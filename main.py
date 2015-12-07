import genetics
import random

import debug




random.seed("YouAreNotAloneWhenAtWork...")



world = genetics.Population(10)
print "World INIT", world

world.calcFitness("012345")
world.sort("fitness")

print "World Sort",world

world.generateNewGeneration(fromCopy=False )
print "World Next Gen",world.nextGeneration

world.setPopulationToNext()
world.calcFitness("012345")
world.sort("fitness")
print "World Sort",world
world.generateNewGeneration(fromCopy=False )

world.setPopulationToNext()
world.calcFitness("012345")
world.sort("fitness")
print "World Sort",world
#world.generateNewGeneration(fromCopy=False )
print world.myHist(world.individuals[0])


