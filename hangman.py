#Whelcom! This is the game of hangman
#This game chooses a random word from a list.
# The user has the chance to guess the number of 
# letters of that word, otherwise he loses. 
# Note: At first, the user must know that the word is a
# multi-letter word that the developer of the program has
# added another option to, so that after each step,
#  the user knows the number of remaining opportunities. 
from random import choice as c
l=["Orange","Apple","Pineapple","Table",
 "Desk","Bedroom","Wolf",
  "Cat","Cow","Zebra","Goat","electricity"
 "donkey", "hardware", "xerox", "transistor",
 "computer'", "desktop","engineering", 
 "hangman", "circuit", "imagination", "robot", 
 "memory", "power", 
 "submarine", "chess", "resistance", "matrix",
 "function", "laser", "mechanism", 
 'bodyguard', 'titanic', 'global', 'ozone', 
 'bridge', 'technology', 'spider',
 'pyramid', 'sphere', 'member', 'warning', 
 'yourself', 'screen', 'language',
 'system', 'internet', 'parameter', 'traffic', 
 'network', 'filter', 'nucleus', 
 'automatic', 'microphone', 'cassette', 
 'operation', 'country', 'beautiful']
def cmp(g,d):
    output=0
    if g==d:
        output=1
        
    return output   
    
D=c(l)
i=0
result=0
print("YOU ONLY HAVE ",len(D)," CHANCES:) ")
for i in range(len(D)):
    print("YOU STIIL HAVE ",len(D)-i," CHANCES:) ")
    g=input(" Guesse the word:) ")
    result=cmp(g,D)
    if result==1:
        print(" Well done! You won this set:)) ")
        break
    else:
        print(" Oops! You lost this set. You can try again:(( ")
print("The correct answer is: ",D)
if i+1==len(D):
    print("GAME OVER!")
    