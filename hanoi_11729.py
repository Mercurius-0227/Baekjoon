n=int(input())
i=0
top=[]
while i<n:
    num=int(input())
    if num:
        top.append(num)
    else:
        top.pop()
    i+=1
print(sum(top))