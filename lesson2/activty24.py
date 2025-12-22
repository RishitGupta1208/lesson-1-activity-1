def func():
    cal=0
    for i in range(11):
        if i%2==0:
            cal+=i
        continue
    print("sum of all even numbers till 10 is",cal)
ty=func()