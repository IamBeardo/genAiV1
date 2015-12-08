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
        if target == "": target="0123456789"

        tmp = 0
        for i in range(len(cmpString)):
            tmp2 = ord(target[i]) - ord(cmpString[i])   # diff between chars
            tmp3=tmp2                                   # save orig diff for debug
            tmp2 *= tmp2                                # ^2 to increase fitness in bigger diff and convert to unsigned
            tmp += tmp2                                 # update over-all diff for string. High is bigger diff.
            #print i,tmp, tmp2, tmp3
        self.fitness=tmp
        return cmpString

    def __init__(self, genformat=string.digits, genlen=10, setValue=""):
        self.meMutated = -1
        self.fitness = 0
        self.genformat = genformat
        self.genlen = genlen
        if setValue =="":
            self.body = ''.join(random.choice(self.genformat) for i in xrange(genlen))
        else:
            self.body = setValue
        Gen.mycount += 1
        self.P1=None
        self.P2=None

    def __repr__(self):
        return self.body + "'" + str(self.fitness)

    def __del__(self):
        Gen.mycount -= 1
        return None
    #########################################################################################################
    # Class Gen:
    # Set sorting and compare functions.
    #########################################################################################################
    def __lt__(self,other):
        #print " Got self {} and {} :< {} ".format(self.fitness,other.fitness,self.fitness<other.fitness)
        return other.fitness < self.fitness

    def __eq__(self,other):
        try:
            return other.fitness==self.fitness
        except:
            return False

    def __setslice__(self, i, j, sequence):
        print "APA!!!!"

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
        self.generation=0
        self.solved=False
        self.nrOfIndividuals = nrofindividuals
        self.nextGeneration = []
        self.individuals = []
        self.individuals = [Gen() for i in xrange(nrofindividuals)]
        print "setting up initial population..."

    def __repr__(self):
        return "".join("<" + str(i) + "> " for i in self.individuals)

    def setPopulationToNext(self):
        self.generation= self.generation+1
        self.individuals = self.nextGeneration
        self.nextGeneration = None


    def getAnsastors(self,aGen,tStartHistory=""):
        tStartHistory= tStartHistory+"{"+str(aGen)+" "
        if aGen.P1 == None:
            tP1="[P1: DEVINE]"
        else:
            tP1=self.getAnsastors(aGen.P1,"[P1")+"]"
        if aGen.P2 == None:
            tP2="[P2: DEVINE]"
        else:
            tP2=self.getAnsastors(aGen.P2,"[P2:")+"]"

        tRet=tP1+tP2+"}"
        return tStartHistory+tRet

    def fitness(self):
        return  "Generation:{} Min: {} Max: {} Best Ind: {}, P1: {} P2 {}, Mutation: {}".format(self.generation,self.min,self.max,self.bestIndividual,self.bestIndividual.P1, self.bestIndividual.P2, self.bestIndividual.meMutated)

    #########################################################################################################
    #
    # Function CalcFitness:
    #       Calc fitness for each member of individuals, and overall statistics for the current population
    #               target: if set, will update class var for fitness, that will be used in coming CalcFitness calls
    #
    #########################################################################################################

    def calcFitness(self,target=""):
        if target <> "":
            self.target=target

        self.min=-1
        self.max=-1
        self.bestIndividual=None

        for i in self.individuals:
            i.calcFitness(self.target)
            tF=i.fitness
            if self.min==-1:
                self.min,self.max=tF,tF
                self.bestIndividual=i
            if tF< self.min:
                self.min=tF
                self.bestIndividual=i
            if tF> self.max: self.max=tF

        if self.bestIndividual.fitness == 0:
            self.solved=True

    def sort(self,byWhat="fitness"):
        if byWhat=="fitness":
            self.individuals.sort(reverse=True )

    def mutate(self,pop,rate):
        for indi in pop:
            tR=random.random()
            #print tR
            if (tR < rate):
                #print indi.body
                tPos = random.randint(0,len(indi.body)-1)
                tRan = random.choice(string.digits)
                indi.body = indi.body[:tPos] + tRan + indi.body[tPos+1:]
                indi.meMutated=tPos
                #print "len::", len(indi.body), "["+indi.body+"]"
                #print "tpos",tPos

                #indi.body[random.randint(0,len(indi.body))]=str(random.choice(string.digits))



    def defineEvolution(self,evolutionMatrix):
        self.evolutionMatrix = evolutionMatrix

    #########################################################################################################
    # Class Population:
    # GenerateNewGeneration:
    #       _oldGeneration: from what collection of individuals to form the new population
    #       fromCopy:       make a copy of original population before starting some functions could modify
    #                       original population.
    #########################################################################################################

    def generateNewGeneration(self, _oldGeneration=None, popsize=-1, fromCopy=True, tSettings=""):
        if not _oldGeneration: _oldGeneration=self.individuals
        if fromCopy:    oldGeneration = _oldGeneration.__getslice__(0, len(_oldGeneration))
        else:           oldGeneration=_oldGeneration

        if popsize == -1: popsize=len(oldGeneration)
        oldGeneration.sort(reverse=True)
        for cmdList in self.evolutionMatrix:
            #print cmdList
            if cmdList[0] == "ClearNextGen":
                self.nextGeneration=[]
            elif cmdList[0] == "GetElits":
                #print len(oldGeneration)*cmdList[1]
                self.nextGeneration = self.getElites(oldGeneration,[int(len(oldGeneration)*cmdList[1]),cmdList[2]])
                #print self.nextGeneration
                #print "sizeNow",len(self.nextGeneration)
            elif cmdList[0] == "GenChildren":
                _numberOfItems = int(len(oldGeneration)*cmdList[1]/2)
                #print _numberOfItems
                _crosspoint = cmdList[2]
                _kids = cmdList[3]
                _function = cmdList[4]
                _selectRange = int(len(oldGeneration)*cmdList[5])
                _compareNumber = cmdList[6]
                _returnNumber = cmdList[7]

                if _function == "GetMates":
                    for i in range(0,_numberOfItems):
                        newChildren=self.genChildren(self.getMates(oldGeneration),_crosspoint=_crosspoint)
                        for c in newChildren:
                            self.nextGeneration.append(c)
                    #print self.nextGeneration
                    #print "sizeNow",len(self.nextGeneration)
        exit
        #                           #No , actionOnSource




    def genChildren(self, _parents,_crosspoint=-1,_siblings=True):
        p1,p2 = _parents[0], _parents[1]


        #random crosspoint
        if _crosspoint == -1:
            _crosspoint = random.randint(0,len(p1.body))
        # waited crosspoint
        if _crosspoint == -2:                           #waited crossover
            _totalscore = p1.fitness + p2.fitness       # as in: p1.fitness = 30 p2.fitness = 70, totalscore = 100
            p1w = (float(p1.fitness) /_totalscore)      # p1w = 30/100 = 0,3
            _crosspoint = int(len(p1.body)*(1-p1w))     # and reverted so 70% is taken from p1 due to more (less if better) "fitness"

            #print p1.fitness, p2.fitness, _totalscore, p1w, _crosspoint


        c1= Gen( genlen=p1.genlen )
        c2= Gen( genlen=p1.genlen )

        c1.body = p1.body[:3] + p2.body[_crosspoint:]
        #print c1
        _children=[c1]

        if _siblings:
            c2.body = p2.body[:3] + p1.body[_crosspoint:]
            _children.append(c2)

        #print "Parents:   ", p1, p2
        #print "Crossing @:",_crosspoint
        #print "children:  ", c1, c2
        for c in _children:
            c.P1=p1
            c.P2=p2
            #print isinstance( c.P2,Gen)

        return _children


    def getMates(self,_fromPopulation,allowSelfBread=False):

        #print "Mates from pop", _fromPopulation
        p1=self.getParentFromTournament(_fromPopulation, 3,1)
        p2=p1
        _parents =p1
        #print "PARENTS", _parents
        while p2 == p1:
            p2=self.getParentFromTournament(_fromPopulation,3,1)
            #print "Parent1,Parent2", p1,p2, "Parents equal:",p1==p2

        _parents.append(p2[0])

        return _parents

    def getParentFromTournament(self, _fromPopulation,_nrOfSelection, _parentsReturned):
        #print "Tour from pop", _fromPopulation

        #_tmpList= [_fromPopulation[random.randint(0,len(_fromPopulation)-1)] for i in range(_nrOfSelection)]
        _tmpList=[]
        for i in range(_nrOfSelection):
            _tmpList.append(_fromPopulation[random.randint(0,len(_fromPopulation)-1)])


        _tmpList.sort(reverse=True)

        #print "tmplist", _tmpList
        return _tmpList[:_parentsReturned]

    def getElites(self,fromPopulation, elitesParam):
        """ getElites ( fromPopulation: list of class Gen: Objects
                        elitesParam:    list of [   INT:numberOfElitesToExtract,
                                                    STR:('keep'/'remove') items from fromPopulation
                        return LIST: subset of fromPopulation """
        #return fromPopulation.__getslice__(0,elitesParam[0])

        _numberOfElites , _action = elitesParam
        #print "Setting Elits:",_numberOfElites , _action
        _tmpList = fromPopulation[:_numberOfElites]
        #print _tmpList
        if _action == 'keep': pass
        elif _action == 'remove': fromPopulation[:_numberOfElites] = []
        else: raise NameError("recived: {}".format(_action))
        for t in _tmpList:
            t.P1 = t
            t.P2 = None

        return _tmpList

    #########################################################################################################
    #
    # Set sorting and compare functions.
    #
    #########################################################################################################
    def __lt__(self, other):
        print "lt called"
        return 1==1




