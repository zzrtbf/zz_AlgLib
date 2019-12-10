# <center>zz_AlgLib</center>

<center><font size=5>A zz open source algorithms library.</font></center>
</br>
<center>made by B17010918张政</center>


## Features
* Made by Python, easy to use
* Great code structure
* Collective intelligent algorithms
</br>

## Class Particles
```
class Particles(object):
    def __init__(self, dimension): 
        self.pos = np.empty(dimension)  # now position
        self.vel = np.zeros(dimension)  # now velocity
        self.fit_value = 0 # now fit value
        self.p_best_pos = np.empty(dimension)   # personal best position
        self.p_best_fit_value = 0 # personal best fit value
```

## Class PSO_ALG
* init
```
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
```
* init_move
```
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
```

* move_particles
```
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
```

* cal_fit_value
```
# Calculate the fit value of each particle
    def cal_fit_value(self):
        for part in self.part_list:
            part.fit_value = self.fit_func(part.pos)
            # if now value < p_best_value : update information
            if part.fit_value < part.p_best_fit_value:
                part.p_best_fit_value = part.fit_value
                part.p_best_pos = part.pos
```

* change_global_best_value
```
# change the global best fit value
    def change_global_best_value(self):
        for part in self.part_list:
            if part.fit_value < self.g_best_fit_value:
                self.g_best_fit_value = part.fit_value
                self.g_best_pos = part.pos
```
* output_result
```
# output the best position and fit value
def output_result(self):
    print("The best solution is " + str(self.g_best_pos))
    print("The best fit value is " + str(self.g_best_fit_value))
```
* start_evolution
```
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
```

</br>