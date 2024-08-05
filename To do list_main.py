#This program takes a list 
# of your tasks and displays
# them, and by taking input in while, 
# it deletes one or more of 
# them as you wish, until your list ends.
def POP(y,x):
    # x=list
    # if x!=int:
    #     x=int(x)
    if y!=list:
        y=list(y)
    d= y.remove(x)
    return d
def To_do_list(works):
    global l2
    l2=[]
    
    while 1:
        n=input("Which activity do you want to remove?")
        if n=="":
            print("your new list is: ",l)
            break
        if n in l:
            l.remove(n)
            if len(l)>0:
                print("new list: ", l)
            else:
                print("You finished your activities .")
                break
        else:
            print("this activity is not in your list. ")
        
            
l=[]
while 1: 
    works=input("works: ")
    l.append(works)
    if works=='':
        l.remove(works)
        print(l," are your works ")
        To_do_list(works)
        break

    
    