#2447번. 별 찍기
#2020.07.29
#방법1.재귀함수 사용
def space(n):
    return " "*n

def make_star(n):
    print("***"*(n//3))
    print("* *"*(n//3))
    print("***"*(n//3))

    if n!=3:
        for i in range(2):
            if i==0: make_star(n//3)*space(n//3)*make_star(n//3)
            else: make_star(n//3)*(n//3)


n=int(input())
make_star(n)
