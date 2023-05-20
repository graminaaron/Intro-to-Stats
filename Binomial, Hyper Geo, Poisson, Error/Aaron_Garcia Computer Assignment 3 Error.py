#Name/ID #: Aaron Garcia/030556771
#Name of Assignment: Computer Assignment 3
#Due Date: Nov 27th, 2022
#Submission Date: Nov 26th, 2022

def main():
    # --------------------BEGIN FUNDIMENTAL DATA ENTRY------------------------
    X = 0
    while X <= 0:
        try:
            X = int(input("Input size of subpopulation of interest. "))
            if X <= 0:
                print("You must enter an integer greater than or equal to one.")
        except ValueError:
            print("You must enter an integer.")

    not_X = 0
    while not_X <= 0:
        try:
            not_X = int(input("Input size of subpopulation not of interest. "))
            if not_X <= 0:
                print("You mus enter an integer greater than or equal to one.")
        except ValueError:
            print("You must enter an integer.")
    N = X + not_X
    p = X / N #instead of inputting the probability, we calculate it
    # --------------------END FUNDIMENTAL DATA ENTRY------------------------

    # --------------------BEGIN BINOMIAL------------------------
    n = 0
    while (n <= 0) or (n > X):
        try:
            n = int(input("Input size of sample. "))
            if n <= 0:
                print("You must enter an integer greater than or equal to one.")
            elif n > X:
                print("The sample cannot be larger than the subpopulation of interest.")
        except ValueError:
            print("You must enter an integer.")

    def comb(a, b): # Determines combinations using factorial function.
        import math
        numerator = math.factorial(a)
        denominator = math.factorial((a - b))*math.factorial(b)
        quotient = int(numerator / denominator)
        return quotient

    def binom(n, p): # binomial probability mass function.
        X = [] # Empty list to record horizontal axis values.
        prob = [] # Empty list to record vertical axis values.
        for x in range(0, n + 1):
            X.append(x)
            c = comb(n, x) # Calling combinations function.
            y = c*(p**x)*((1 - p)**(n - x))
            prob.append(y)
        print('trial \t probability')
        print('number')
        for i in range(0, n + 1):
            print(format(X[i], '3d'),format(prob[i], '13.4f'))
        return X, prob

    def bigraph():
        import matplotlib.pyplot as plt
        x, y = binom(n,p) # Calling binomial function.
        bar_width = 1
        plt.bar(x,y,bar_width, color=('y'))
        #plt.plot(x,y,'r+')
        trials = str(n) # Casting data types for use in labels.
        success = str(p) # Same as previous line.
        plt.title('Binomial')
        plt.xlabel('Trials = '+trials)
        plt.ylabel('Probability of success = '+success)
        plt.show()

    bigraph() #Graph binomial function.
    # --------------------END BINOMIAL------------------------

    # --------------------BEGIN HYPERGEOMETRIC------------------------
    n = -1
    while n<= 0:
        try:
            n = int(input("Enter the number of trials. "))
            if n < 0:
                print("You cannot enter a negative number.")
        except ValueError:
            print("You did not enter an integer greater than or equal to one.")

    def hyper(N, X, n):
        H = []
        p = []
        for x in range(0, n + 1):
            H.append(x)
            denominator = comb(N, n)
            factor1 = comb(X, x)
            factor2 = comb(N - X, n - x)
            ans = ((factor1*factor2)/denominator)
            p.append(ans)
        return H, p

    def hypergraph():
        import matplotlib.pyplot as plt
        x, y = hyper(N, X, n) # Calling hypergeometric function.
        print(x)
        print(y)
        bar_width = 1
        plt.bar(x,y,bar_width, color=('r'))
        plt.title('Hypergeometric')
        plt.show()

    hypergraph() # Graph hypergeometric function.

    # --------------------END HYPERGEOMETRIC------------------------

    # --------------------BEGIN ERROR------------------------
    def errorgraph(): #calc and graph error
        import matplotlib.pyplot as plt
        x, y = binom(n,p) # Calling binomial function.
        print('Binomial')
        print(x)
        print(y)
        w, z = hyper(N, X, n) # Calling hypergeometric function.
        print('Hypergeometric')
        print(w)
        print(z)
        a = [] #initialize error arrays
        b = []
        if (len(y) == len(z)):
            a = x
            for i in range(len(y)):
                b.append(y[i] - z[i]) #binomial - hypergeo
        elif (len(y) > len(z)): #if binomial array is larger, only calc error function to hypergeo array
            a = w
            for i in range(len(z)):
                b.append(y[i] - z[i]) #binomial - hypergeo
        elif (len(y) < len(z)): #if hypergeo array is larger, only calc error function to binomial array
            a = x
            for i in range(len(y)):
                b.append(y[i] - z[i]) #binomial - hypergeo
        print('Error')
        print(a)
        print(b)
        bar_width = 1
        plt.bar(a,b,bar_width, color=('g'))
        plt.title('Error')
        plt.show()

    errorgraph()# Graph error function
    # --------------------END ERROR------------------------
main()