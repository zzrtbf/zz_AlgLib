##### Welcome to zz DE Algorithm #####

import numpy as np
from random import random, randint,sample
from intell_alg import Candidate, Intell_alg

class DE_Cand(Candidate):
    def __init__(self, dim):
        super().__init__(dim)
        self.new_soln = np.zeros(dim)  # new generation solution

class DE_alg(Intell_alg):
    def __init__(self, prob, pop_size, max_iter):
        super().__init__(prob, pop_size, max_iter)
        # population list generated by de_candidate
        self.pop_list = [DE_Cand(self.dim) for i in range(self.pop_size)]
        # set DE parameters
        self.F, self.Cr = 0.1, 0.6

    # Deduce
    def deduce(self):
        for cand in self.pop_list:
            # generate family list
            while(1):
                fam_list = sample(self.pop_list, 3)
                if cand not in fam_list:
                    break
            for i in range(self.dim):
                coin = random()
                if( (coin < self.Cr) | (i == randint(0,self.dim)) ):
                    cand.new_soln[i] = fam_list[0].soln[i] + self.F * (fam_list[1].soln[i] - fam_list[i].soln[i])
                else:
                    cand.new_soln[i] = cand.soln[i]
        for cand in self.pop_list:
            new_value = self.fit_func(cand.new_soln)
            if new_value < cand.fit_value:
                cand.fit_value = new_value
                cand.soln = cand.new_soln
                cand.best_fit_value = new_value
                cand.best_soln = cand.new_soln
        self.bound()

    # Conclude
    def conclude(self):
        self.update_global()



        








