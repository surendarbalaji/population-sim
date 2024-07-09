import numpy as np
import matplotlib.pyplot as plt

X0 = 98  #Initial population
t_end = 100000  #Final Year
K = 8e9  #Carrying capacity
mu = 0.05  #Average growth rate
sigma = 0.1  #Standard deviation of growth rate
dt = 1  #Timestep (1 year)

total_individuals = 0  #running birth total
life_expectancy = 80 #80 years average life expectancy

fluctuation_threshold = 7.5e9  #Population threshold for introducing major fluctuations
fluctuation_range = 5e7  #Range of fluctuations
threshold_reached = False

t = np.arange(0, t_end + dt, dt) #generates intervals from 0 to t_end
X = np.zeros(len(t)) #initialise population array
X[0] = X0

for i in range(1, len(t)):
    r = np.random.normal(mu, sigma)  #generating randomly sampled growth rate
    dXdt = r * X[i-1] * (1 - X[i-1] / K)  #Logistic growth model
    
    #Apply random fluctuations after reaching the threshold
    if X[i-1] > fluctuation_threshold:
        dW = np.random.uniform(-fluctuation_range, fluctuation_range)
    else:
        dW = 0
    
    dX = dXdt * dt + dW
    X[i] = X[i-1] + dX

    #Adds population to running total every 80 years
    if threshold_reached and i % life_expectancy == 0:
        total_individuals += X[i]

    if not threshold_reached and X[i] > fluctuation_threshold:
        threshold_reached = True
        count_start = i

print(f"~{total_individuals:,} people lived from the year {count_start} to the year {t_end}")

plt.plot(t, X)
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Stochastic Simulation of Population Growth")
plt.grid(True)
plt.show()