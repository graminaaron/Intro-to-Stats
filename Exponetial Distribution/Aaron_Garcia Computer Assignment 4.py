#Name/ID #: Aaron Garcia/030556771
#Name of Assignment: Computer Assignment 4
#Due Date: Dec 3rd, 2022
#Submission Date: Nov 30th, 2022

import math
import random
import matplotlib.pyplot as plt

def main():
    n = 22500
    X = [] #uniform rv
    Y = [] #exponential rv
    L = 1 #parameter for exponential rv
    for i in range(n):
        r=random.uniform(0, 1)
        X.append(r) #list of uniformly distributed numbers
        e=-(L)*math.log(r, math.e) #natural log
        Y.append(e) #list of exponentially distributed numbers
    b = max(X)
    a = min(X)
    R = b-a #this is the range
    intervals = int(math.ceil(math.sqrt(n))) #the number of bins
    width = (R/intervals) #the class width
    #-----------------------------------------------------------
    #code for plots
    plt.subplot(2, 1, 1)
    plt.title('N = ' + str(n) + ', sqrt(N) = ' +str(math.sqrt(n)), loc='center')
    plt.hist(X, intervals, density=width, color='r')
    plt.subplot(2, 1, 2)
    plt.hist(Y, intervals, density=width, color='g')
    plt.show()

main()
#%%
