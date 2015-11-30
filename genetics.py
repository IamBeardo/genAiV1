import string
import random




class Gen:
    mycount=0

    def __init__(self,genformat=string.digits,genlen=10):
        self.genformat=genformat
        self.genlen=genlen
        self.body = ''.join(random.choice(self.genformat) for i in xrange(genlen))
        Gen.mycount += 1

    def __repr__(self):
        return self.body

    def __del__(self):
        Gen.mycount-=1
        #print Gen.mycount



class Individual:
    mycount=0

    def __init__():
        Individual.mycount +=1

    def __del__(self):
        Individual.mycount -=1



class Population:




