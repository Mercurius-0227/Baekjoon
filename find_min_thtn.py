#2581 소수
#2020.07.17 완성!!!!!!!!!!!!!!!!!

M=int(input())
N=int(input())

i=0
j=1
k=0
total=0
min_total=0
min_rest=0

for i in range(M,N+1):
    for j in range(2, i):
        rest=i%j
        if i==1:
            mark=1
            lee=False
            break
        elif rest==0:
            mark=1
            lee=False
            break
        else:
            mark=0
            lee=True
        if lee==False:
            mark=1
            break
    if mark==0:
        total+=i
        for k in range(1):
            min_rest=rest
if total==0:
    total=-1
    print(total)
else:
    print(total)
    print(min_rest+M)


            