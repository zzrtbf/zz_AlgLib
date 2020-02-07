from zz_problem import Problem
from zz_pso import PSO_alg
from zz_de import DE_alg
import math

def sphere(soln):
    return sum(pow(soln[i], 2) for i in range(len(soln)))

def rastrigin(soln):
    return 10*len(soln) + sum(pow(soln[i], 2)-10*math.cos(2*math.pi*soln[i]) for i in range(len(soln)))

class Test_prob(Problem):

    def __init__(self):
        super().__init__()
        self.dim = 2                # The dimension of the problem
        self.lower = (-10, -10)     # lower bound (shoule be written by tuple)
        self.upper = (10, 10)       # upper bound 

    # Objective function
    # This fuction should be redefined in the practical problem
    def fit_func(self, soln):
        fit_value = rastrigin(soln)
        return fit_value

prob = Test_prob()
alg = DE_alg(prob)

print("Start thinking")

alg.init_think()
for i in range(alg.max_iter_num):
    alg.deduce()
    alg.conclude()

print("The best solution is " + str(alg.best_soln))
print("The best fit value is " + str(alg.best_fit_value))







