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
            for i in range(len(self.parents)):
                prob = prob[evid[self.parents[0]
            return [1-self.prob[evid[self.parents[0]]][evid[self.parents[1]]], self.prob[evid[self.parents[0]]][evid[self.parents[1]]]]

    def is_empty_parents(self):
        if self.parents:
            return False
        else:
            return True


class BN():
    def __init__(self, gra, prob):
        self.graph
        self.prob

    def computePostProb(self, evid):
        pass

        return 0


    def computeJointProb(self, evid):
        pass

        return 0
