import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint

X0 = [98] #initial population

t = np.linspace(0, 2000,num=2000) #start at year 0, go until year 200, with 2000 intervals

r = 0.05 #growth rate
K = 8e9 #carrying capacity

params = [r, K] #pack values into an array

def sim(variables, t, params):
    X = variables[0]
    
    r = params[0]
    k = params[1]

    dXdt = r*X * (1 - X/k) #logistic growth model

    return([dXdt])

X = odeint(sim, X0, t, args=(params,)) #integrate to get the population over time

index_8billion = np.argmax(X >= 8e9) #find the first year where the population is greater than 8 billion

measurement_interval = 80 #we will count the population every 80 years

measurements = len(t) - index_8billion #the period over which we will measure
total_individuals = 0
for i in range(index_8billion, len(t), measurement_interval):
    total_individuals += X[i, 0] #adds the current population to a running total every 80 years

print(f"~{total_individuals:,} people lived from the year {index_8billion} to the year 2000")

plt.plot(t, X[:,0])
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()