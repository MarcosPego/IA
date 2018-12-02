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
        pass

        return 0

    def computeJointProb(self, evid):
        starting_prob = []
        final_prob=[]
        jointProb = 1
        for i in range(len(evid)):
            starting_prob.append(self.prob[i].computeProb(evid))
            final_prob.append(starting_prob[i][evid[i]])
            jointProb *= final_prob[i]

        return jointProb
