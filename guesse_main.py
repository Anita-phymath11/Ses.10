# This program is actually a
# function-based number guessing game.
# First, the computer takes a number
# range from the user and then selects a
# random number in that range. 
# The user has 5 chances to guess 
# the number correctly.
from random import randint as r
rand=int(input(" ENTER A NUMBER: "))
rand1=int(input(" ENTER ANOTHER NUMBER: "))
Q=r(rand,rand1)
# print(Q)
iri=5
for i in range(iri):
    print("IRITATION: ",i+1)
    guess=int(input("ENTER A NUMBER: "))
    if guess<Q:
        print(" LESS! ")
    elif guess>Q:
        print(" MORE! ")
    elif guess==Q:
        print(" YOU WON:) ")
        break
    elif i==4 and guess!=Q:
        print(" GAME OVER:( ")
        print(" THE CORRECT ANSWER IS: ",Q)
        break
print(" THE GAME FINISHED:) the correct answer: ", Q)