uw=(input(" please enter a word: "))
ul=(input(" please enter a letter to check ocurrence: "))
i=0
count=0
while (i<len(uw)):
    if (uw[i]==ul):
        count+=1
    i+=1
print(count)