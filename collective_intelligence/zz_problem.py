##### zz problem class #####

import numpy as np

# Problem Class
class Problem(object):
    def __init__(self, dim, lower, upper):
        self.dim = dim      # The dimension of the problem
        self.lower = lower  # lower bound (shoule be written by tuple)
        self.upper = upper  # upper bound 

    # Objective function
    # This fuction should be redefined in the practical problem
    def fit_func(self, soln):
        # default sphere function
        return sum(pow(soln[i], 2) for i in range(len(soln)))
 


