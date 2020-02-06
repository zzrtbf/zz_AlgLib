##### zz problem class #####

import numpy as np

# Problem Class
class Problem(object):
    def __init__(self):
        self.dim = 1        # The dimension of the problem
        self.lower = (0,)   # lower bound (shoule be written by tuple)
        self.upper = (1,)   # upper bound 

    # Objective function
    # This fuction should be redefined in the practical problem
    def fit_func(self, soln):
        fit_value = 0
        for ans in soln:
            fit_value = fit_value + ans
        return fit_value
 


