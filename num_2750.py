#2750번: 수 정렬하기(오름차순)
#2020.07.21
#함수 이용
n=int(input())

list_a=[]
for i in range(n):
    list_a.append(int(input()))
list_a.sort()
for i in range(n):
    print(list_a[i])

#버블 정렬 이용
n=int(input())

list_a=[]
for i in range(n):
    list_a.append(int(input()))
for num in range(n,0,-1):
    for i in range(num):
        if i ==(num-1):
            break
        if list_a[i]>list_a[i+1]:
            b=list_a[i]
            list_a[i]=list_a[i+1]
            list_a[i+1]=b
for i in range(n):
    print(list_a[i])

#삽입 정렬 이용
n=int(input())

list_a=[]
for i in range(n):
    list_a.append(int(input()))

for i in range(0,n):
    for j in range(i, -1, -1):
        if (j+1)==n:
            break
        if list_a[j]>list_a[j+1]:
            b=list_a[j]
            list_a[j]=list_a[j+1]
            list_a[j+1]=b
        
for i in range(n):
    print(list_a[i])
