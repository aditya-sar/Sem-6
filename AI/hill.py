import random
import math

def objFunc(x):
    return math.sin(x)-math.cos(2*x)

def hillClimb(x, step, maxItr):
    fx = objFunc(x)

    for _ in range(maxItr):
        dx = (random.random()*2 - 1)*step
        next_x = x+dx
        next_fx = objFunc(next_x)

        if next_fx > fx:
            fx = next_fx
            x = next_x
    
    return x

if __name__ == "__main__":

	x = 1
	step = 0.01
	maxItr = 1000

	res = hillClimb(x, step, maxItr)
	print(f'Point found: {res}\nf(x): {objFunc(res)}')
