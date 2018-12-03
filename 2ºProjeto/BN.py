# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob

    def computeProb(self, evid):
        if self.is_empty_parents():
            return [1-self.prob[0], self.prob[0]]
        elif len(self.parents)==1:
            return [1-self.prob[evid[self.parents[0]]], self.prob[evid[self.parents[0]]]]
        else:
            prob = self.prob
            for i in range(len(self.parents)):
                prob = prob[evid[self.parents[i]]]
            return [1-prob, prob]

    def is_empty_parents(self):
        if self.parents:
            return False
        else:
            return True


class BN():
    def __init__(self, gra, prob):
        self.graph = gra
        self.prob  = prob

    def computePostProb(self, evid):
        prob1=0
        prob2=0
        array_probs = []
        print(self.prob[0].computeProb((1,1,1,1,1)))
        for i in range(2):
            for j in range(2):
                prob1 += self.prob[0].computeProb((1,i,j,1,1))[1]*self.prob[1].computeProb((1,i,j,1,1))[i]*self.prob[2].computeProb((1,i,j,1,1))[j]*self.prob[3].computeProb((1,i,j,1,1))[1]*self.prob[4].computeProb((1,i,j,1,1))[1]
                #prob += self.prob[0].prob[0]*self.prob[1].prob[i]*self.prob[2].prob[i][j]*self.prob[3].prob[j]*self.prob[4].prob[j]
                print(self.prob[0].computeProb((1,i,j,1,1))[1],self.prob[1].computeProb((1,i,j,1,1))[i],self.prob[2].computeProb((1,i,j,1,1))[j],self.prob[3].computeProb((1,i,j,1,1))[1],self.prob[4].computeProb((1,i,j,1,1))[1])

        #for i in range(2):
        #    for j in range(2):
        #        prob2 += self.prob[0].computeProb((1,i,j,1,1))[0]*self.prob[1].computeProb((1,i,j,1,1))[i]*self.prob[2].computeProb((1,i,j,1,1))[j]*self.prob[3].computeProb((1,i,j,1,1))[1]*self.prob[4].computeProb((1,i,j,1,1))[1]

        #print(prob1)
        #print(prob2)
        #alpha = 1/ (prob1+prob2)
        #print(prob1+prob2)
        #print(alpha)
        return prob1/2.1

    def computeJointProb(self, evid):
        starting_prob = []
        final_prob=[]
        jointProb = 1
        for i in range(len(evid)):
            starting_prob.append(self.prob[i].computeProb(evid))
            final_prob.append(starting_prob[i][evid[i]])
            jointProb *= final_prob[i]

        return jointProb
