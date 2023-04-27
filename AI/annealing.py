import random
import math

def objFunc(x):
    return math.sin(x)-math.cos(2*x)

def simulatedAnnealing(x, maxItr, T):
    fx = objFunc(x)
    Tmin = 0.0001

    for _ in range(maxItr):
        alpha = 0.99
        T = T*alpha

        dx = (random.random()*2-1)*T
        next_x = x+dx
        next_fx = objFunc(next_x)

        if next_fx > fx or random.random() < math.exp((next_fx-fx)/T):
            x = next_x
            fx = next_fx

        if T < Tmin:
            break
    
    return x


if __name__ == "__main__":

    x = 1
    maxIter = 1000
    T = 1.0 

    res = simulatedAnnealing(x, maxIter, T)

    print(f'Point found: {res}\nf(x): {objFunc(res)}')
