i=0
k=0

n=int(input("정수 입력(3<=n<=5000)>"))

if n%5==0:
    i=n//5
    print(i)

elif n<5:
    if n==3:
        i=1
        print(i)
    elif n==4:
        i=-1
        print(i)

else:
    i=n//5
    n=n%5
    if n==1:
        i=i-1
        n=n+5
        i=i+2
        print(i)
    elif n==2:
        i=i-2
        n=n+10
        i=i+4
        print(i)
    elif n==3:
        i=i+1
        print(i)
    elif n==4:
        i=i-1
        n=n+5
        i=i+3
        print(i)
    else:
        i=-1
        print(i)
    
