import string
import random




class Gen:
    mycount=0

    def __init__(self,genformat=string.digits,genlen=10):
        self.fittnes=0
        self.genformat=genformat
        self.genlen=genlen
        self.body = ''.join(random.choice(self.genformat) for i in xrange(genlen))
        Gen.mycount += 1

    def __repr__(self):
        return self.body

    def __del__(self):
        Gen.mycount-=1
        #print Gen.mycount
    def calcFittnes(self,target="012345"):
        tmp=0
        for i  in range(len(self.body)):

            tmp2= ord(target[i])-ord(self.body[i])
            tmp2=tmp2*tmp2
            tmp = tmp2+tmp
            print tmp,tmp2
        #tFittnes+= ord(x)-ord(y)
        print(target,self.body)

        self.fittnes=tmp




class Individual:
    mycount=0

    def __init__():
        Individual.mycount +=1

    def __del__(self):
        Individual.mycount -=1



class Population:

    def __init__(self,nrofindividuals):
        self.individuals = [Gen() for i in xrange(nrofindividuals)]
        pass
    def __repr__(self):
        return "".join("["+str(i)+"] " for i in self.individuals)




