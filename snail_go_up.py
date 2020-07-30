total=0
day=0

A,B,V=input().split()
A=int(A)
B=int(B)
V=int(V)

while True:
    total+=A
    day+=1
    if total==V:
        print(day)
        break
    total-=B
    if total==V:
        print(day)
        break

