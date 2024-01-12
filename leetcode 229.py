n=int(input())
lst=[3,2,3]
dct={}
for i in lst:
    dct[i]=lst.count(i)
for i,j in dct.items():
    if j>len(lst)//3:
        print(i)