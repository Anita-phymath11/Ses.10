# This program changes the list of
# names in such a way that it gives
# a random number to each person in 
# the list and prints all the 
# names and a random number in front
# of each one.
from random import randint as r
ll=int(input("num1: "))
lll=int(input("num2(end): "))
l_name=["Anita","Dina","Nafas","Nahid","Kiana","Negar","Narges"]
for i in (l_name):
    a=r(ll,lll)
    print(i,":",a)