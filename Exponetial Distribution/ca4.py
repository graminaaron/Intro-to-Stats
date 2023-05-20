import math
import random
import matplotlib.pyplot as plt


def main():
    n = 100000
    x = []  # Uniform RV
    y = []  # Exponential RV
    lamda = 1  # parameter for exponential RV
    for i in range(n):
        r = random.uniform(0, 1)
        x.append(r)  # a list of uniformly distributed numbers
        e = -(lamda)*math.log(r, math.e)  # natural log
        y.append(e)  # a list of exponentially distributed numbers
    b = max(x)
    a = min(x)
    R = b - a  # This is the range
    intervals = int(math.ceil(math.sqrt(n)))  # The number of bins
    width = (R/intervals)  # The class width
    # ------------------------------------------------------------
    # Code for plots
    plt.subplot(2, 1, 1)
    plt.hist(x, intervals, density=width)
    plt.subplot(2, 1, 2)
    plt.hist(y, intervals, density=width)
    plt.show()


main()
