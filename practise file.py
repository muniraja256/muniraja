x=5
def H():
 y=6
 for row in range(x):
    for col in range(y):
        if (col==0 and row>=0) :
            print("B",end=" ")
        elif  (col>=1 and row==2) or (col==5 and row>=0):
            print("Y", end=" ")
        else:
            print(" ",end=" ")
    print()
H()
print(" \n ")
def A():
    y=9
    for row in range(x):
        for col in range(y):
            if (row+col==4 and col <=4) or (row == 2 and (col==4 or col==3 or col==5))\
                    or ((row==1 and col==5) or (row==2 and col==6) or (row==3 and col==7) or (row==4 and col==8)):
                print("M", end=" ")
            else:
                print(" ", end=" ")
        print()
A()
print(" \n ")
def P():
    y=3
    for row in range(x):
        for col in range(y):
            if (col==0 and row>=0) or (row==0 and col>0) or (col==2 and (row==1 or row==2)) or (col==1 and row==2):
                print("U", end=" ")
            else:
                print(" ", end=" ")


        print()
P()
print(" \n ")
def p():
    y=3
    for row in range(x):
        for col in range(y):
            if (col==0 and row>=0) or (row==0 and col>0) or (col==2 and (row==1 or row==2)) or (col==1 and row==2):
                print("N", end=" ")
            else:
                print("",end=" ")
        print()
P()
def Y():
    y=5
    for row in range(x):
        for col in range(y):
            if (col==2 and row>=2) or (row==col and col<2) or (col==3 and row==1) or (col==4 and row==0):
                print("I", end=" ")
            else:
                print(" ", end=" ")

        print()
Y()
print(" \n ")
def two():
    y=4
    for row in range(x):
        for col in range(y):
            if (col == 0 and row > 0 and row!=2) or (col==1 and row>=0 and row!=1 and row!=3)\
                    or (col == 2 and row>=0 and row!=2 and row!=3) or (col==3 and row==4):
                print("R", end=" ")
            else:
                print(" ", end=" ")

        print()
two()
print(" \n ")
def zero():
    y=4
    for row in range(x):
        for col in range(y):
            if (col == 0 and row > 0 and row!=4) or (row==0 and col>0 and col!=3) or( row==4 and col>0 and col!=3)\
                    or (col ==3 and row>0 and row!=4 ) :
                print("A", end=" ")
            else:
                print(" ", end=" ")

        print()
zero()
print(" \n ")
def Two():
    y=4
    for row in range(x):
        for col in range(y):
            if (col == 0 and row > 0 and row != 2) or (col == 1 and row >= 0 and row != 1 and row != 3) \
                    or (col == 2 and row >= 0 and row != 2 and row != 3) or (col == 3 and row == 4):

                print("J", end=" ")
            else:
                print(" ", end=" ")

        print()
Two()
print("\r")
def One():
    y=5
    for row in range(x):
        for col in range(y):
            if (row == 4 and col>=0) or (col==2 and row>=0 )\
                    or (row == 1 and col==1 ):
                print("A", end=" ")
            else:
                print(" ", end=" ")

        print()
print("\n")
One()
print("\n\n\n")
print(''' By muniraja''')




































