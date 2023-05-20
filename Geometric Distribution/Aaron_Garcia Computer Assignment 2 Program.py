#Name/ID #: Aaron Garcia/030556771
#Name of Assignment: Computer Assignment 2
#Due Date: Oct 29th, 2022
#Submission Date: Oct 27th, 2022

#Overall Problem:
#You have a coin with the probability of heads being 𝑝. Toss the coin until a head comes up for
#the first time. What are the chances of that happening on an odd-numbered toss?

import random

print("In this computer assignment, we will be testing for \n "
      "the probability of the amount of coin flips it takes \n "
      "to recieve heads on an odd number.")

def ExerciseThree():
    # default probabilities to test
    # for the ones listed on the rubric
    arr_p = [(1/5),(1/2),(2/3)]

    """
    #if you want to add more probabilities to test for, uncomment this line.
    cont = True
    c = bool(input('Would you like to add any other probabilites? (y/n): '))
    if(c == 'y' or c == 'Y' or c == 'yes' or c == 'Yes'):
        cont == True

    while(cont):
        prob = float(input('Enter the probability of success. '))
        arr_p.insert(prob)
        c = bool(input('Continue Adding Probabilities? (y/n): '))
        if(c == 'n' or c == 'N'):
            cont == False
    """

    # Number of experiment repetitions
    # (NOT the same as the number of
    # individual trials in a given experiment)
    reps = 1000000

    # For each probability:
    for p in arr_p:
        fav_outcomes = 0
        # do "reps" num of repetitions of the
        # same experiment using the probability
        for rep in range(reps):
            t=0 # Number of Trials = Failures + 1
            # BEGIN EXPERIMENT:
            while(True): # While we keep getting a failure,
                t = t+1 # Increment Trials
                r = random.uniform(0,1)
                if r < p:
                    #print('h', end=' ') # Debug
                    break #Once we succeed, break
                #else:
                    #print('t', end='') # Debug
            if (t % 2 == 1):
                #print(('Odd! (' + str(t) + ')'), end=' ')# Debug
                fav_outcomes += 1
        print("", end="\n")
        print("Stats for coin flipping heads with probability = \n" + str(p))
        print("Final favorable outcomes: \n" + str(fav_outcomes) + "/" + str(reps))
        print("Estimated probability of landing on an odd number first: \n" + str(float(fav_outcomes/reps)))



ExerciseThree()


