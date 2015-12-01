import genetics
import random
import string



random.seed("YouAreNotAloneWhenAtWork...")

a=genetics.Gen(string.digits,6)
b=genetics.Gen(string.digits,6)
c=genetics.Gen(string.digits,6)






world=genetics.Population(10)



a.calcFittnes()
print a.fittnes