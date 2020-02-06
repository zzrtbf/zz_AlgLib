##### Welcome to ZZ PSO Algorithm #####

import numpy as np
from intell_alg import Candidate, Intell_alg

# PSO Algorithms
class PSO_alg(Intell_alg):

    def __init__(self, prob):
        super().__init__(prob)    # Intell_alg.__init__()
        self.vel_list = np.zeros((self.pop_size, prob.dim))  # velocity list
        # set PSO parameters
        # this program uses LDW(Linearly Decreasing Weight) to adjust w
        self.c1, self.c2, self.w_ini, self.w_end = 2, 2, 0.9, 0.4
    
    # Deduce
    def deduce(self):
        w = (self.w_end - self.w_ini)/self.max_iter_num * self.now_iter_num \
            + self.w_ini
        for i in range(self.pop_size):
            # calculate velocity array
            self.vel_list[i] = w*self.vel_list[i] + \
                self.c1 * np.random.rand() * (self.pop_list[i].best_soln - self.pop_list[i].soln) + \
                self.c2 * np.random.rand() * (self.best_soln - self.pop_list[i].soln)
            # update solution
            self.pop_list[i].soln = self.pop_list[i].soln + self.vel_list[i]
   
    # Conclude
    def conclude(self):           
        self.cal_fit_value()
        self.update_cand()
        self.update_global()
        self.now_iter_num += 1


