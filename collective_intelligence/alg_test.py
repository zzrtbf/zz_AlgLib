from zz_problem import Problem
from zz_pso import PSO_alg
from zz_de import DE_alg
from math_test_func import sphere, rastrigin, ackley

dimension = 2           # the dimension of the problem
lower = (-10, -10)      # lower bound (shoule be written by tuple)
upper = (10, 10)        # upper bound
pop_size = 12           # the number of the candidate
max_iter = 1000         # max iteration number


class Test_prob(Problem):

    def __init__(self, dim, lower, upper):
        super().__init__(dim, lower, upper)

    # Objective function
    # This fuction should be redefined in the practical problem
    def fit_func(self, soln):
        fit_value = ackley(soln)
        return fit_value

prob = Test_prob(dimension, lower, upper)
alg = PSO_alg(prob, pop_size, max_iter)

print("Start thinking")

alg.init_think()
for i in range(alg.max_iter_num):
    alg.deduce()
    alg.conclude()

print("The best solution is " + str(alg.best_soln))
print("The best fit value is " + str(alg.best_fit_value))







