import string
import random

#########################################################################################################
#
# Class Gen:
#
#########################################################################################################

class Gen:
    mycount = 0

    def calcFitness(self, target=""):
        cmpString=self.body
        if target == "": target="012345"

        tmp = 0
        #print("target ",target,"Self ", cmpString,"Raw Fitness ")
        for i in range(len(cmpString)):
            tmp2 = ord(target[i]) - ord(cmpString[i])   # diff between chars
            tmp3=tmp2                                   # save orig diff for debug
            tmp2 *= tmp2                                # ^2 to increase fitness in bigger diff and convert to unsigned
            tmp += tmp2                                 # update over-all diff for string. High is bigger diff.
            #print tmp, tmp2, tmp3
        self.fitness=tmp

        return cmpString

    def __init__(self, genformat=string.digits, genlen=10):
        self.fitness = 0
        self.genformat = genformat
        self.genlen = genlen
        self.body = ''.join(random.choice(self.genformat) for i in xrange(genlen))
        Gen.mycount += 1

    def __repr__(self):
        return self.body + "[" + str(self.fitness) + "]"

    def __del__(self):
        Gen.mycount -= 1
        return None


    #########################################################################################################
    #
    # Set sorting and compare functions.
    #
    #########################################################################################################
    def __lt__(self,other):
        #print " Got self {} and {} :< {} ".format(self.fitness,other.fitness,self.fitness<other.fitness)
        return other.fitness < self.fitness

    def __eq__(self,other):
        return other.fitness==self.fitness


#########################################################################################################
#
# Class Individual:
#
#########################################################################################################
class Individual:
    mycount = 0

    def __init__(self):
        Individual.mycount += 1

    def __del__(self):
        Individual.mycount -= 1

#########################################################################################################
#
# Class Population:
#
#########################################################################################################
class Population:
    def __init__(self, nrofindividuals):
        self.nrOfIndividuals = nrofindividuals
        self.nextGeneration = []
        self.individuals = [Gen(genlen=6) for i in xrange(nrofindividuals)]
        print "setting up initial population..."

    def __repr__(self):
        return "".join("<" + str(i) + "> " for i in self.individuals)

    def calcFitness(self,target=""):
        for i in self.individuals:
            i.calcFitness(target)

    def sort(self,byWhat="fitness"):
        if byWhat=="fitness":
            self.individuals.sort()

    def generateNewGeneration(self, _oldGeneration=None, popsize=-1, fromCopy=True):

        if not _oldGeneration: _oldGeneration=self.individuals
        if fromCopy:    oldGeneration = _oldGeneration.__getslice__(0, len(_oldGeneration))
        else:           oldGeneration=_oldGeneration

        if popsize == -1: popsize=len(oldGeneration)
        oldGeneration.sort()

        #                           #No , actionOnSource
        _elites                 =   [2  , 'remove']           # 'keep'/'remove'
        _tournamentBreading     = 4
        _directMutation         = 0

        print "aaaaaaaaaaaaaaaaa"


        self.nextGeneration =self.getElites(oldGeneration,_elites)

        #print self.individuals
        #print oldGeneration
        #print self.nextGeneration




    def getElites(self,fromPopulation, elitesParam):
        """ getElites ( fromPopulation: list of class Gen: Objects
                        elitesParam:    list of [   INT:numberOfElitesToExtract,
                                                    STR:('keep'/'remove') items from fromPopulation
                        return LIST: subset of fromPopulation """
        #return fromPopulation.__getslice__(0,elitesParam[0])

        _numberOfElites , _action = elitesParam
        print _numberOfElites , _action
        _tmpList = fromPopulation[:_numberOfElites]
        if _action == 'keep': pass
        elif _action == 'remove': fromPopulation[:_numberOfElites] = []
        else: raise NameError("recived: {}".format(_action))



        return _tmpList




    #########################################################################################################
    #
    # Set sorting and compare functions.
    #
    #########################################################################################################
    def __lt__(self, other):
        print "lt called"
        return 1==1




