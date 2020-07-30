#10872번. 팩토리얼
#2020.07.28

def factorial(n):
    if n>=1:
        return n*factorial(n-1)
    else:
        return 1

n=int(input())

print(factorial(n))