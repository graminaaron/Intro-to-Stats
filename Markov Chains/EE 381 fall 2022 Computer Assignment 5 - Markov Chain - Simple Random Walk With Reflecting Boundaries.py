'''
Coputer Assingment 5 (The last assignment!)
For the program below suggested values of p are 0.25, 0.50. 0.75.
Try 5 < N < 10.
Make the Jump bigger than 10 but not too much larger than 25.
Record some (more than 2 less than 6) of your input / outputs and upload as a PDF.
Satisfactory submission is worth 3 points..
'''

# Program to Simulate a Random Walk on N

p = float(input("Enter the probability of a right step. "))
S = int(input("Enter a starting position. "))
N = int(input("Enter the right booundary. "))
Jump = int(input("Enter the number of steps. "))

import random

for i in range(Jump):
    
    if S == 0:
        S = 1
    elif S == N:
        S = N - 1
    elif ((S < N) & (S > 0)):
        
        r = random.uniform(0,1)
        
        if r < p:
            S = S + 1
        else:
            S = S - 1
    print(S)

#%%
