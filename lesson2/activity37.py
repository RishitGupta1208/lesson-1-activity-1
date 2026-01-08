def match_words(words):
    ctr=0
    list=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            list.append(word)
    print("list of words which have the first and last letter same are",list)
    return ctr
count=match_words(['aba','cggdc','1221'])