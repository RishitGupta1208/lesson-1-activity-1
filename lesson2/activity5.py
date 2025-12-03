r=int(input("please enter the number of rows:"))
num=1
print("floyd's triangle")
for i in range(r):
    for j in range(i+1):
        print(num,end="")
        num+=1
    print()