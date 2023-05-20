'''
Discription: Simulate a Bernoulli R.V.
'''
import random

p = float(input('Enter the probability of success. '))
T = int(input('Enter number of trials. '))

for j in range(T):
    
    r = random.uniform(0,1)
    if r < p:
        print('1', end=' ') # Success
    else:
        print('0', end=' ') # Failure
    
