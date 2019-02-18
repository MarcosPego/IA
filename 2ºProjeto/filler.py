




			if self.counter >= 10:
				a=np.random.randint(2)
				self.alpha = a

			elif self.alpha == 1:
				a=0
				self.counter -= 1
				if(self.counter == 0):
					self.counter = np.random.randint(100)
					self.alpha=0
			else:
				a=1
				self.counter -= 1
				if(self.counter == 0):
					self.counter = np.random.randint(100)
					self.alpha=1



if self.alpha == 1:
    a=0
    self.alpha=0
else:
    a=1
    self.alpha=1


for i in range(len(evid)):
    if evid[i] == -1:

        probs *= self.prob[i].prob[0]
    elif evid[i] == []:
        array_probs.append(self.prob[i].prob)
    else:
        pass
print(array_probs)
return probs/2


        for i in range(len(evid)):
            prob1 += self.prob[0].computeProb(evid[i])[evid[i][0]]*self.prob[1].computeProb(evid[i])[evid[i][1]]*self.prob[2].computeProb(evid[i])[evid[i][2]]*self.prob[3].computeProb(evid[i])[evid[i][3]]*self.prob[4].computeProb(evid[i])[evid[i][4]]


        final_p_evid = self.define_final_possible_evid(evid)
        evid = self.make_possible_evid(final_p_evid)
        for i in range(len(evid)):
            prob1 += self.prob[0].computeProb(evid[i])[evid[i][0]]*self.prob[1].computeProb(evid[i])[evid[i][1]*self.prob[2].computeProb(evid[i])[evid[i][2]]*self.prob[3].computeProb(evid[i])[evid[i][3]]*self.prob[4].computeProb(evid[i])[evid[i][4]]





"""
Created on Mon Oct 15 15:53:25 2018

@author: mlopes
"""

import numpy as np
np.set_printoptions(precision=4, suppress=True)

from BN import *

gra = [[],[],[0,1],[2],[2],[0,1,5]]
ev = (0,0,1,1,1,0,1)

p1 = Node( np.array([.001]), gra[0] )                   # burglary
print( "p1 false %.4e p1 true %.4e" % (p1.computeProb(ev)[0] , p1.computeProb(ev)[1]))

p2 = Node( np.array([.002]), gra[1] )                   # earthquake

p3 = Node( np.array([[.001,.29],[.94,.95]]), gra[2] )   # alarm
print( "p1 = 1, p2 = 1, p3 false %.4e p3 true %.4e" % (p3.computeProb(ev)[0] , p3.computeProb(ev)[1]))

p4 = Node( np.array([.05,.9]), gra[3] )                 # johncalls


p5 = Node( np.array([.01,.7]), gra[4] )                 # marycalls

p6 = Node( np.array([.003]), gra[0] )

p7 = Node( np.array([[[.001,.002],[.29,.32]],[[.94,0.97],[.95,.98]]]), gra[5] )
print( "p1 = 1, p2 = 1, p6=1  p7 false %.4e p7 true %.4e" % (p7.computeProb(ev)[0] , p7.computeProb(ev)[1]))


prob = [p1,p2,p3,p4,p5,p6,p7]

gra = [[],[],[0,1],[2],[2],[0,1,5]]
bn = BN(gra, prob)
jp = []
for e1 in [0,1]:
    for e2 in [0,1]:
        for e3 in [0,1]:
            for e4 in [0,1]:
                for e5 in [0,1]:
                    for e6 in [0,1]:
                        for e7 in [0,1]:
                            jp.append(bn.computeJointProb((e1, e2, e3, e4, e5, e6, e7)))
