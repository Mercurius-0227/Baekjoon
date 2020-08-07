def hanoi(원반개수, 시작, 목표, 보조):
    if 원반개수==1:
        print(시작, '->', 목표)
        return
    hanoi(원반개수-1, 시작, 보조, 목표)
    print(시작, '->', 목표)
    hanoi(원반개수-1, 보조, 목표, 시작)


n=int(input())
hanoi(n,1,3,2)