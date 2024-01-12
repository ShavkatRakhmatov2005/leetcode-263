def reverseString(s:list[str])->None:
    l,r=0,len(s)-1
    while l<r:
        s[l],s[r]=s[r],s[l]
        l,r=l+1,l-1
print(reverseString(["h","e","l","l","o"]))