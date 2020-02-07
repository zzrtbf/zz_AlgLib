import math

# sphere function
def sphere(soln):
    return sum(pow(soln[i], 2) for i in range(len(soln)))

# rastrigin function
def rastrigin(soln):
    return 10*len(soln) + sum(pow(soln[i], 2)-10*math.cos(2*math.pi*soln[i]) for i in range(len(soln)))

# ackley function
def ackley(soln):
    return 1 - math.exp(-10 * math.sqrt(sum(pow(soln[i], 2) for i in range(len(soln))) / len(soln))) + \
        math.e - math.exp(sum(math.cos(2*math.pi*soln[i]) for i in range(len(soln))) / len(soln) )





