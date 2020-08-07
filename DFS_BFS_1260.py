#1260번. DFS와 BFS
#2020.08.06

#DFS(깊이 우선 탐색)
def go_dfs(line,n,m,v,cnt):
    dfs=[]
    dfs.append(v)
    for i in range(n):
        k=[]
        for j in range(len(line)):
            if dfs[i]==line[j][0]: k.append(line[j][1])
            if dfs[i]==line[j][1]: k.append(line[j][0])
        if len(dfs)!=cnt:
            go=[]
            for t in range(len(k)):
                for h in range(len(dfs)):
                    if k[t]==dfs[h]: 
                        go.append(k[t])
            for x in range(len(go)):
                k.remove(go[x])
            if len(k)!=0:
                dfs.append(min(k)) 
        else: 
            print(dfs)
            break

#BFS(너비 우선 탐색)
def go_bfs(line,n,m,v,cnt):
    bfs=[]
    bfs.append(v)
    i=-1
    while len(bfs)<=cnt:
        i+=1
        k=[]
        for j in range(len(line)):
            if bfs[i]==line[j][0]: k.append(line[j][1])
            if bfs[i]==line[j][1]: k.append(line[j][0])
        if len(bfs)!=cnt:
            go=[]
            for t in range(len(k)):
                for h in range(len(bfs)):
                    if k[t]==bfs[h]:
                        go.append(k[t])
            for x in range(len(go)):
                k.remove(go[x])
            if len(k)!=0:
                for _ in range(len(k)):
                    bfs.append(min(k))
                    k.remove(min(k))
        else: 
            print(bfs)
            break


n,m,v=map(int,input().split())
line=[]
for i in range(m):
    imsi=list(map(int,input().split()))
    line.append(imsi)
if n<=m: cnt=n
else: cnt=m+1

go_dfs(line,n,m,v,cnt)

go_bfs(line,n,m,v,cnt)