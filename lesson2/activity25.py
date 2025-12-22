def shutdown():
    a=input("do you want to save your open work:")
    if a=='yes':
        print("moving on")
    elif a=='no':
        print("aborting shutdown")
        return
    else:
        print("sorry")
        return
    b=input("do you want to close the programs:")
    if b=='yes':
        print("moving on")
    elif b=='no':
        print("aborting shutdown")
        return
    else:
        print("sorry")
        return
    c=input("do you really want to shut down:")
    if c=='yes':
        print("shutting down")
    elif c=='no':
        print("aborting sutdown")
    else:
        print("sorry")
ty=shutdown()
print("thank you")