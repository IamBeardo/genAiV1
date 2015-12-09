import genetics
import random

#random.seed("YouAreNotAloneWhenAtWork...")
random.seed("YouAreNotAloneWhenAtWor")

tSettings =     [
                    ["ParentTracking",2],
                    ["ClearNextGen",],
                    ["GetElits", 0, "keep"],
                    ["GenChildren",             # GenChildren
                        1,                      # 1 = rest of list
                        5,                     # -1 crosspoint random
                        2,                      # kids to create
                        "GetMates",             # TournamentGet
                            0.9,                 # select from top 90%
                            3,                  # select 3
                            1                   # return 1 of the selected
                    ]
                ]

_totalGeneration=0
_count=0
for count in xrange(1):
    print "==== Gens:", genetics.Gen.mycount

    world = genetics.Population(10)       #population
    world.defineEvolution(tSettings)
    world.generateRandomPopulation()
    #world.calcFitness("0123456789")
    #print world.fitness(True)

    for i in range(100):                    #generations
        world.calcFitness("0123456789")
        print world.fitness(True)
        if world.solved:
            break
        world.sort("fitness")
        #print world
        world.generateNewGeneration(fromCopy=False )
        world.mutate(world.nextGeneration,0.15)
        world.setPopulationToNext()


    _count = _count +10
    _totalGeneration = _totalGeneration + world.generation
    #print world.fitness()
    print "avrgeneration {}".format(_totalGeneration/_count)

    world.printAnsestors(world.Ansastors(world.bestIndividual))






print "==== DONE ===="
#print world.individuals([world.individuals[0]])



