##### Welcome to the zz Intelligent Algorithms #####
import numpy as np
from zz_problem import Problem

# Candidate Class
class Candidate(object):
    
    def __init__(self, dim): 
        self.soln = np.zeros(dim)  # now position
        self.fit_value = 0 # now fit value
        self.best_soln = np.zeros(dim)   # personal best position
        self.best_fit_value = 0 # personal best fit value

# Intelligent Algorithm Class
class Intell_alg(object):

    def __init__(self, prob):
        self.dim = prob.dim         # the dimension of the problem
        self.pop_size = 12    # the number of candidate 
        self.fit_func = prob.fit_func   # objective function
        self.best_soln = np.zeros(prob.dim) # global best soln
        self.best_fit_value = 0     # global best fit value

        self.now_iter_num = 0       # the now iteration number
        self.max_iter_num = 1000    # the max iteration number

        self.lower = prob.lower     # lower bound 
        self.upper = prob.upper     # upper bound

        # population list
        self.pop_list = [Candidate(self.dim) for i in range(self.pop_size)]
    
    # calculate the fit value for every candidate
    # and update best soln if now < best
    def cal_fit_value(self):
        for cand in self.pop_list:
            # calculate fit value
            cand.fit_value = self.fit_func(cand.soln)
    
    # update personal best soln and fit value if now < best
    def update_cand(self):
        for cand in self.pop_list:
            if cand.fit_value < cand.best_fit_value:
                cand.best_fit_value = cand.fit_value
                cand.best_soln = cand.soln
    
    # find global best soln and update global best
    def update_global(self):
        for cand in self.pop_list:
            if cand.best_fit_value < self.best_fit_value:
                self.best_fit_value = cand.best_fit_value
                self.best_soln = cand.best_soln

    # initialize the think process
    def init_think(self):
        self.now_iter_num = 1   # set iteration time to one
        # random generate solution, and set to personal best
        for cand in self.pop_list:
            cand.soln = np.random.uniform(self.lower, self.upper)
            cand.fit_value = self.fit_func(cand.soln)
            cand.best_soln = cand.soln
            cand.best_fit_value = cand.fit_value
        self.best_fit_value = self.pop_list[0].best_fit_value
        self.best_soln = self.pop_list[0].best_soln
        for cand in self.pop_list:
            if cand.fit_value < self.best_fit_value:
                self.best_fit_value = cand.fit_value
                self.best_soln = cand.soln

    # Deduce
    def deduce(self):
        pass

    # Conclude
    def conclude(self):
        pass


