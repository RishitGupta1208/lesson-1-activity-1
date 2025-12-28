try:
    num1, num2=eval(input("enter 2 number seperated by a comma:"))
    result= num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("can't divide a number with zero")
except SyntaxError:
    print("comma is missing enter 2 numbers seperated by s comma like this 1, 2 ahgadjgdsgdjjshhfh")
except:
    print("Wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")