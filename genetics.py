import string
import random



class Gen:
    mycount = 0

    def calcFitness(self, target=""):
        cmpString=self.body
        if target == "": target="012345"

        #print "target {} {}".format(target,len(target))
        #print "self.body {} {}".format(cmpString,len(cmpString))

        tmp = 0
        for i in range(len(cmpString)):
            tmp2 = ord(target[i]) - ord(cmpString[i])
            tmp2 *= tmp2  # ^2 to increase fitness in bigger diff and convert to unsigned
            tmp += tmp2
            print tmp, tmp2
            #tFittnes+= ord(x)-ord(y)
        self.fitness=tmp
        print(target, cmpString,self.fitness)
        return cmpString

    def __init__(self, genformat=string.digits, genlen=10):
        self.fitness = 0
        self.genformat = genformat
        self.genlen = genlen
        self.body = ''.join(random.choice(self.genformat) for i in xrange(genlen))
        Gen.mycount += 1

    def __repr__(self):
        return self.body

    def __del__(self):
        Gen.mycount -= 1
        #print Gen.mycount






class Individual:
    mycount = 0

    def __init__(self):
        Individual.mycount += 1

    def __del__(self):
        Individual.mycount -= 1


class Population:
    def __init__(self, nrofindividuals):
        self.individuals = [Gen(genlen=6) for i in xrange(nrofindividuals)]
        print "setting up population..."


    def __repr__(self):
        return "".join("[" + str(i) + "] " for i in self.individuals)

    def calcFitness(self,target=""):
        for i in self.individuals.__getslice__(2,3):
            i.calcFitness(target)
            print i.fitness



