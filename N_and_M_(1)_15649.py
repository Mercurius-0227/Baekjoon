#15649번. n과 m(1)
#2020.07.30
#방법1.함수 사용
#from itertools import permutations
#
#n,m=map(int,input().split())
#a=[]
#for i in range(1,n+1):
#    a.append(i)
#b=list(permutations(a,m))
#
#for j in range(len(b)):
#    print(' '.join(map(str,b[j])))



#방법2. 함수 사용하지 않고 풀기
#n,m=map(int,input().split())
#check=[False]*(n+1)
#a=[0]*m

#def go(index,n,m):
#    if index==m:
#        for i in range(m):
#            print(a[i],end=' ')
#        print()

#        return
#    for i in range(1, n+1):
#        if check[i]:
#            continue
#        check[i]=True
#        a[index]=i
#        go(index+1,n,m)
#        check[i]=False

#go(0,n,m)


