'''
The program below plots the Poisson distribution for different
values of the parameter.  Run the progam for values of the parameter:
2, 4, 6, 8, 10, 12.  What happens to the Poisson distribution as the value
of the parameter changes?  How might it play a roll in the application
of the central limit theorem?
Submit with the relevant plots and answers in your PDF.
'''

#Name/ID #: Aaron Garcia/030556771
#Name of Assignment: Computer Assignment 3
#Due Date: Nov 27th, 2022
#Submission Date: Nov 26th, 2022

L = float(input("Enter the value of the Poisson parameter. "))

N = 25 # Number of probabilities

import math

P = math.exp(-L)

X = [0] # Horizontal axis
Y = [P] # Vertical axis

for i in range(N):
    if i > 0:
        P = P*(L/i)
        X.append(i)
        Y.append(P)
    print(i, P)
print(X)
print(Y)

import matplotlib.pyplot as plt


plt.plot(X,Y,'r+')
plt.show()


