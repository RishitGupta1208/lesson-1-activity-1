rowNum = 3 #initialised number of rows 5

space = rowNum-1

for i in range(1, rowNum+1): #loops for rows
    for j in range(1,space+1):
        print(end="")
    space-=1
    for j in range(2*i-1):
        print(end="*")
    print()