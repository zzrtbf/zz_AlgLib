##### Welcome to ZZ PSO Algorithm #####

import numpy as np
import random
inf = float('inf')

# Particles
class Particles(object):

    def __init__(self, dimension): 
        self.pos = np.empty(dimension)  # now position
        self.vel = np.zeros(dimension)  # now velocity
        self.fit_value = 0 # now fit value
        self.p_best_pos = np.empty(dimension)   # personal best position
        self.p_best_fit_value = 0 # personal best fit value

# PSO Algorithms
class PSO_ALG(object):

    def __init__(self, dimension, fit_func, lower, upper, part_num, max_iter_num, c1, c2, w_ini, w_end):
        self.dimension = dimension  # The dimension of problems
        self.fit_func = fit_func  # The function to calculate the fit value of one particle
        self.lower = lower  # The upper bound and lower bound of the particles
        self.upper = upper
        self.part_num = part_num  # The number of particles
        self.max_iter_num = max_iter_num  # The maximum number of iteration
        # The variances for calculation
        self.c1, self.c2, self.w_ini, self.w_end = c1, c2, w_ini, w_end
        
        self.now_iter_num = 0  # now iteration number
        self.g_best_pos = np.empty(dimension)  # global best position
        self.g_best_fit_value = inf # global best fit value
        
    # Initialize the movement
    def init_move(self):
        self.now_iter_num = 1
        self.part_list = [Particles(self.dimension)] * self.part_num
        for part in self.part_list:
            part.pos = np.random.uniform(self.lower, self.upper)
            part.fit_value = self.fit_func(part.pos)
            part.p_best_pos = part.pos
            part.p_best_fit_value = part.fit_value
            if part.fit_value < self.g_best_fit_value:
                self.g_best_fit_value = part.fit_value
                self.g_best_pos = part.pos
    
    # Movement
    def move_particles(self):
        # calculate w by LDW(Linearly Dicreasing Weight)
        w = (self.w_end - self.w_ini)/self.max_iter_num * self.now_iter_num
        for part in self.part_list:
            # calculate velocity
            part.vel = w * part.vel + \
            self.c1 * np.random.rand() * (part.p_best_pos - part.pos) + \
            self.c2 * np.random.rand() * (self.g_best_pos - part.pos)
            # calculate position
            part.pos = part.pos + part.vel

    # Calculate the fit value of each particle
    def cal_fit_value(self):
        for part in self.part_list:
            part.fit_value = self.fit_func(part.pos)
            # if now value < p_best_value : update information
            if part.fit_value < part.p_best_fit_value:
                part.p_best_fit_value = part.fit_value
                part.p_best_pos = part.pos
            
    # change the global best fit value
    def change_global_best_value(self):
        for part in self.part_list:
            if part.fit_value < self.g_best_fit_value:
                self.g_best_fit_value = part.fit_value
                self.g_best_pos = part.pos
    
    # output the best position and fit value
    def output_result(self):
        print("The best solution is " + str(self.g_best_pos))
        print("The best fit value is " + str(self.g_best_fit_value))

    # an auto method to run PSO algorithm
    def start_evolution(self):
        self.init_move()
        while (self.now_iter_num <= self.max_iter_num):
            self.move_particles()
            self.cal_fit_value()
            self.change_global_best_value()
            self.now_iter_num += 1
        self.output_result()
        return self.g_best_pos, self.g_best_fit_value


# fit function 
# y = x^2
def fit_func(part_pos):
    fit_value = pow(part_pos[0], 2) + pow(part_pos[1], 2)
    return fit_value

# fit test function
def fit_test_func(part_pos):
    pass

# PSO test function
def PSO_test():
    # Variance of problems
    dimension = 2   # The dimension of the particles
    # The upper bound and lower bound of the particles, should be given as tuples
    lower, upper = (-8, -10), (8, 10)
    
    # Variance of PSO
    part_num = 100 # The number of particles
    max_iter_num = 1000
    c1 = 2
    c2 = 2
    w_ini = 0.9
    w_end = 0.4

    zz_pso = PSO_ALG(dimension, fit_func, lower, upper, part_num, max_iter_num, c1, c2, w_ini, w_end)

    zz_pso.start_evolution()

PSO_test()


