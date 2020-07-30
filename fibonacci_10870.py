#10870번. 피보나치 수5
#2020.07.28

def fibonacci(n):
    if n>=2:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return n

n=int(input())

print(fibonacci(n))