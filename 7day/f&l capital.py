s="hello"
s="".join([i for i in s if not i.isdigit()])
result=[]
for word in s.split():
    if len(word)>1:
        word=word[0].upper()+word[1:-1]+word[-1].upper()
    else:
        word=word.upper()
        result.append(word)
        
        print(" ".join(result))
        
