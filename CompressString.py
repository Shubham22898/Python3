#string compression

s = input()
count = 1
res=[]
for i in range(1,len(s)):
    if(s[i]==s[i-1]):
        count+=1
    else:
        res.append([count,int(s[i-1])])
        count=1
res.append([count,int(s[-1])])
res=list(map(tuple,res))
print(*res)
    
