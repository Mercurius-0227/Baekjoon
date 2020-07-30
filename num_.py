#2750번: 수 정렬하기
#2020.07.21

n=int(input())

list_a=[]
for i in range(n):
    list_a.append(int(input()))
list_a.sort()
for i in range(n):
    print(list_a[i])