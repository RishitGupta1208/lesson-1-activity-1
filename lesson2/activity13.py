def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multi(p,q):
    return p*q
def div(p,q):
    return p/q
print("please choose an operation")
print("add/addition,sub/subtraction,multi/multiplication,div/division")
choice=input(" please enter the operation you choose: ")
num1=int(input("please enter number1:"))
num2=int(input("please enter number2:"))
if choice=="add":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="sub":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=="multi":
    print(num1,"*",num2,"=",multi(num1,num2))
elif choice=="div":
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("invalid format")