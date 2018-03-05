from random import * #this pulls the information on random numbers from the system,i think. something like that
pricechange = uniform(.6, 1.4) #generates a floating point number between the peramiters
pricechange = '%.2f' % round(pricechange, 2) #long story short, this rounds it to the hundreds place
print pricechange
