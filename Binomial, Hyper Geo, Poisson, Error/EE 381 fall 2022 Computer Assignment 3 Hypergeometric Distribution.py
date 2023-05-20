'''
Computer Assignment 3
Hypergeometric Distribution
If you discover any errors in this program contact the programmer responsible.
Questions?
'''

def main():
 # -------------------Input and Error Traps-----------------------------------   
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
# ------------------End Input-------------------------------------------------
    N = X + not_X
    def comb(a, b):
        import math
        numerator = math.factorial(a)
        denominator = math.factorial((a - b))*math.factorial(b)
        quotient = int(numerator / denominator)
        return quotient
      
    def hyper(N, X, n):
        H = []
        p = []
        for x in range(0, n + 1):
            H.append(x)
            denominator = comb(N, X)
            factor1 = comb(X, x)
            factor2 = comb(N - X, n - x)
            ans = ((factor1*factor2)/denominator)
            p.append(ans)
        return H, p
    
    def graph():
        import matplotlib.pyplot as plt
        x, y = hyper(N, X, n)
        bar_width = 1
        plt.bar(x,y,bar_width, color=('r'))
        plt.title('Hypergeometric')
        plt.show()
    
    graph()
        
main()

