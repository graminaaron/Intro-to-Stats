'''
Example 'Balls in Cans'
Probability and Stochastic Processes
F. Solomon (1987), page 190.
Proposed Computer Solution (Not guaranteed to be free of erros).
To solve the problem this way we need to write the code for the experiment.
The variable 'Can' is a list with the location of each ball.
The numbers 1 through 5 are randolly assigned (repititions allowed) to the elements of 'Can'.
With the experiemnt complete the outcome is tested in the single alternative decision structure.
When each ball is in a different can the 'Sum' of favorable outcomes is incremented by one.
The solution is the ratio of this 'Sum' to the total number of experiments performed.
When the user runs this pprogram keep changing the number 'K' of experiments.
The user should observe a corresponding change in the answers.

The Original program was change to simulate 3 firms chosing
3 months out of the calendar year at random to do their auditing.
If the months all land on different values, that is a favorable outcome.
'''

import random # Using Pythons Random Function

Sum = 0 # Initialize count of number of favorable outcomes. (accumulator variable).

months = [0, 0, 0] # Identifies which month is chosen.

K = 1000 # The number of experiments.

for k in range(K): # Total number of experiments to be performed.

# ---------------------------------------------------
# The experiment starts.                            #
    for i in range(3):                              # For the number of
        month_Number = random.randrange(1,13)       # Pick a random number between 1 and 12 (months)
        months[i] = month_Number                    # Place each number at in the "can array"
# The experiment ends.                              #
# ---------------------------------------------------
# Test for favorable outcomes.       
    if (i == 2)&((months[0] != months[1]) & (months[1] != months[2]) & (months[0] != months[2])):
        Sum = Sum + 1 # Increment the count of favorable outcomes.      

#------------------------ 
# The ratio of favorable outomes to the total number of outcomes.
print(Sum / K)
