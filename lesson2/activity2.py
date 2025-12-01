lr=int(input(" please enter the lower range: "))
ur=int(input(" please enter the upper range: "))
print("the prime numbers between",lr,"and",ur,"are")
for num in range(lr,ur+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
            else:
                print(num)