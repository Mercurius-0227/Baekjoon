def fly_Alpha_Centauri(T, list_X, list_Y):
    distance_=0
    for i in range(1, T+1):
        distance_=list_Y[i]-list_X[i]
        jump=1
        go=0
        distance_-=jump*2
        count=0
        count+=2
        go+=jump*2
        while True:
            if distance_>go:
                count+=1
                if distance_-go>(jump+1):
                    jump+=1
                    go+=jump
                    distance-=jump
                else:
                    go+=jump
                    distance-=jump
            elif distance_==go:
                count+=1
                if jump==1:
                    jump+=1
                    go+=jump
                    distance_-=jump
                else:
                    go+=jump
                    distance_-=jump
            else:
                count+=1
                if jump==1:
                    go+=jump
                    distance_-=jump
                else:
                    jump-=1
                    go+=jump
                    distance_-=jump
            if distance_==0:
                break
        print(count)

def make_distance(T):
    list_X=[0]
    list_Y=[0]
    for i in range(T):
        a,b=input().split()
        a=int(a)
        b=int(b)
        list_X.append(a)
        list_Y.append(b)

    fly_Alpha_Centauri(T, list_X, list_Y)

T=int(input())
i=0
make_distance(T)