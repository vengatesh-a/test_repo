n=int(input("Enter no. of rows:"))

#for num of rows

for r in range (1,n):
    #top half
    for s in range (n,r,-1):
        print(" ",end="")
    for st in range (1,2*r):
        print ("*",end="")
    print ("")
#2nd half
for r in range (n,0,-1):
    for s in range (n,r,-1):
        print (" ",end="")
    for st in range (1,2*r):
        print("*",end="")
    print("")
