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
        #print("target ",target,"Self ", cmpString,"Raw Fitness ")
        #print "LEN", len(cmpString)
        for i in range(len(cmpString)):
            tmp2 = ord(target[i]) - ord(cmpString[i])   # diff between chars
            tmp3=tmp2                                   # save orig diff for debug
            tmp2 *= tmp2                                # ^2 to increase fitness in bigger diff and convert to unsigned
            tmp += tmp2                                 # update over-all diff for string. High is bigger diff.
            #print i,tmp, tmp2, tmp3
        self.fitness=tmp

        return cmpString







    def __init__(self, genformat=string.digits, genlen=10, setValue=""):

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
    #
    # Set sorting and compare functions.
    #
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
        self.nrOfIndividuals = nrofindividuals
        self.nextGeneration = []
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

        return "Generation:",self.generation,"Min",self.min,"Max",self.max


    def calcFitness(self,target=""):
        self.min=-1
        self.max=-1

        for i in self.individuals:
            i.calcFitness(target)
            tF=i.fitness
            if self.min==-1:
                self.min,self.max=tF,tF
            if tF< self.min: self.min=tF
            if tF> self.max: self.max=tF




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
                #print "len::", len(indi.body), "["+indi.body+"]"
                #print "tpos",tPos

                #indi.body[random.randint(0,len(indi.body))]=str(random.choice(string.digits))

    def generateNewGeneration(self, _oldGeneration=None, popsize=-1, fromCopy=True):
        #print _oldGeneration, popsize, fromCopy

        if not _oldGeneration: _oldGeneration=self.individuals
        if fromCopy:    oldGeneration = _oldGeneration.__getslice__(0, len(_oldGeneration))
        else:           oldGeneration=_oldGeneration

        if popsize == -1: popsize=len(oldGeneration)
        #print _oldGeneration, popsize, fromCopy
        oldGeneration.sort(reverse=True)
        #print _oldGeneration, popsize, fromCopy


        #                           #No , actionOnSource
        _elites                 =   [10  , 'keep']           # 'keep'/'remove'
        _tournamentBreading     = 4
        _directMutation         = 0


        self.nextGeneration=[]
        self.nextGeneration =self.getElites(oldGeneration,_elites)
       # print "Next Generation after Elits",self.nextGeneration
        #print "Popsize: ", popsize

        for i in range(len(self.nextGeneration),popsize,2):
            newChildren=(self.genChildren(self.getMates(oldGeneration),_crosspoint=3))
            for c in newChildren:
                #print i, self.nextGeneration
                self.nextGeneration.append(c)



    def genChildren(self, _parents,_crosspoint=-1,_siblings=True):
        p1,p2 = _parents[0], _parents[1]
        if _crosspoint == -1:
            _crosspoint = random.randint(0,len(p1))

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




