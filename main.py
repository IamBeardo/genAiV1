import genetics
import random

#random.seed("YouAreNotAloneWhenAtWork...")

tSettings =     [
                    ["ClearNextGen",],
                    ["GetElits", 0.90, "keep"],
                    ["GenChildren",             # GenChildren
                        0.9,                      # 1 = rest of list
                        -2,                     # -1 crosspoint random
                        2,                      # kids to create
                        "GetMates",             # TournamentGet
                            0.9,                 # select from top 90%
                            3,                  # select 3
                            1                   # return 1 of the selected
                    ]
                ]

a="""
world = genetics.Population(100)
world.defineEvolution(tSettings)
world.calcFitness("0123456789")
world.sort("fitness")
print "world after sort", world"""

_totalGeneration=0
_count=0
for count in range(100):
    world = genetics.Population(100)
    world.defineEvolution(tSettings)
    world.calcFitness("0123456789")
    world.sort("fitness")
    for i in range(100):
        world.generateNewGeneration(fromCopy=False )
        print "aaaaaaaaa"
        world.mutate(world.nextGeneration,0.33)
        world.setPopulationToNext()
        world.calcFitness("0123456789")
        world.sort("fitness")
        #print world.fitness()
        if world.solved:
            break

    _count = _count +1
    _totalGeneration = _totalGeneration + world.generation
    print world.fitness()
    print "avrgeneration {}".format(_totalGeneration/_count)


