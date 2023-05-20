
"""
Computer Assignment 3
Binomial Distribution
If you discover any errors in this program contact the programmer responsible.
Questions?
"""

def main():
# --------------------DATA ENTRY & ERROR TRAPS------------------------    
    p = 0
    while (p<=0) or (p>=1):
        try:
            p = float(input("Enter the probability of success. "))
            if (p<=0) or (p>=1):
                print('You did not enter a number between zero and one.')
        except ValueError:
            print("Enter numbers not other characters.")   
    n = -1
    while n<= 0:
        try:
            n = int(input("Enter the number of trials. "))
            if n < 0:
                print("You cannot enter a negative number.")
        except ValueError:
            print("You did not enter an integer greater than or equal to one.")
# ---------------END DATA ENTRY---------------------------------------
    print('\n')
    
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
    
    def graph():
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
    
    graph()
    
main()