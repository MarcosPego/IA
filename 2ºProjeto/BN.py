# Grupo 82, 87701 Ricardo Ferreira, 86472 Marcos Pêgo
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""
import copy


class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob

    def computeProb(self, evid):
        if self.is_empty_parents():
            return [1-self.prob[0], self.prob[0]]
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

    def define_possible_evid(self,evid, control_flag):
        #initial_p_evid = [[1],[0,1],[0,1],[1],[1]]
        initial_p_evid = []
        for i in range(len(evid)):
            if evid[i] == -1:
                if control_flag == 1:
                    initial_p_evid.append([1])
                else:
                    initial_p_evid.append([0])
            elif evid[i] == []:
                initial_p_evid.append([0,1])
            else:
                initial_p_evid.append([evid[i]])
        return initial_p_evid

    def make_possible_evid(self,initial_p_evid):
        i_evid = []
        for i in range(len(initial_p_evid)):
            if len(initial_p_evid[i]) == 1:
                if len(i_evid) == 0:
                    i_evid.append([initial_p_evid[i][0]])
                else:
                    for j in range(len(i_evid)):
                        i_evid[j].extend([initial_p_evid[i][0]])
            else:
                if len(i_evid) == 0:
                    i_evid.append([initial_p_evid[i][0]])
                    i_evid.append([initial_p_evid[i][1]])
                else:
                    new_evid = copy.deepcopy( i_evid)
                    for j in range(len(new_evid)):
                        new_evid[j].extend([initial_p_evid[i][0]])
                    for j in range(len(i_evid)):
                        i_evid[j].extend([initial_p_evid[i][1]])
                    i_evid +=new_evid

        return i_evid

    def computePostProb(self, evid):
        prob1=0
        prob2=0

        initial_p_evid = self.define_possible_evid(evid,1)
        i_evid = self.make_possible_evid(initial_p_evid)
        print(initial_p_evid)
        print(i_evid)

        for i in range(len(i_evid)):
            prob1 += self.computeJointProb(i_evid[i])

        final_p_evid = self.define_possible_evid(evid,0)
        f_evid = self.make_possible_evid(final_p_evid)
        for i in range(len(f_evid)):
            prob2 += self.computeJointProb(f_evid[i])

        return prob1 / ( prob1+prob2)


    def computeJointProb(self, evid):
        starting_prob = []
        final_prob=[]
        jointProb = 1
        for i in range(len(evid)):
            starting_prob.append(self.prob[i].computeProb(evid))
            final_prob.append(starting_prob[i][evid[i]])
            jointProb *= final_prob[i]

        return jointProb
