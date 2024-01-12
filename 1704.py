def halvesAreAlike(s:str):
    orta=len(s)//2
    a=s[:orta]
    b=s[orta:]
    count,count1=0,0
    for i in a:
        if  i.lower() in ['a', 'e', 'i', 'o', 'u']:
            count+=1
    for i in b:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            count1+=1
    if count==count1:
        return True
    else:
        return False
print(halvesAreAlike(input()))

 