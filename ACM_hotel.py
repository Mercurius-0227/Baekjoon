#10250 ACM호텔
#2020.07.18 완성

def best_choice(T, list_floor, list_rum, list_person):
    for i in range(1,T+1):
        ho=(list_person[i]//list_floor[i])+1
        chung=list_person[i]%list_floor[i]
        print(chung,"0",ho)

T=int(input())
list_floor=[0]
list_rum=[0]
list_person=[0]
for i in range(T):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    list_floor.append(a)
    list_rum.append(b)
    list_person.append(c)

best_choice(T, list_floor, list_rum, list_person)

