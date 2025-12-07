#take input from user
rowsize=int(input(" enter number of rows: "))
if rowsize%2==0: #conditons
    halfdiamonrow=int(rowsize/2)
else:
    halfdiamonrow=int(rowsize/2)+1
space=halfdiamonrow-1
#loop for upper part
for i in range(1,halfdiamonrow+1): #loop for rows
    for j in range(1,space+1): #loop for coloumns
        print(end=" ")
    space-=1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
    #incrementing number in each coloumn
        num+=1
    print()
space=1
#loop for lower part
for i in range(1,halfdiamonrow): #loop for rows
    for j in range(1,space+1): #loop for coloumns
        print(end=" ")
    space+=1
    num=1
    for j in range(1,2*(halfdiamonrow-i)):
        print(end=str(num)) #display result
    #incrementing number in each coloumn
        num+=1
    print()