import genetics
import random

import debug




random.seed("YouAreNotAloneWhenAtWork...")



world = genetics.Population(10)
print world

world.calcFitness("012345")
#world.sort("fitness")
print world

world.generateNewGeneration( )
#print world

daaa = debug._debugPrinter()
daaa.off(False)
daaa.p("asdfasdfasdf")


