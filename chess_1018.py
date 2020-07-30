#1018:체스판 다시 칠하기
#2020.07.23
#인생이 피폐해졌어
#머리에 쥐난다
#머리아파

def repaint_chess(list_chess,n,m):
    count=0
    for i in range(0,n-1):
        for j in range(m-1):
            if list_chess[i][j]==list_chess[i+1][j]:
                count+=1
            if list_chess[i][j]==list_chess[i][j+1]:
                count+=1
                #if list_chess[i][j+1]=='W':
                #    list_chess[i][j+1]=list_chess[i][j+1].replace('W','A')
                #else:
                #    list_chess[i][j+1]=list_chess[i][j+1].replace('B','A')
                #del list_chess[i][j+1]
                #list_chess.insert([i][j+1],'A')
            #if list_chess[i][j+1]==list_chess[i+1][j+1]:
            #    count+=1
            #if list_chess[i+1][j]==list_chess[i+1][j+1]: 
            #    count+=1
                #if list_chess[j+1][i]=='W':
                #    list_chess[j+1][i]=list_chess[j+1][i].replace('W','A')
                #else:
                #    list_chess[j+1][i]=list_chess[j+1][i].replace('B','A')
                #del list_chess[j+1][i]
                #list_chess[j+1][i]='A'
    print(count//4)
    #print(list_chess[0].count('A')+list_chess[1].count('A')+
    #    list_chess[2].count('A')+list_chess[3].count('A')+list_chess[4].count('A')+
    #    list_chess[5].count('A')+list_chess[6].count('A')+list_chess[7].count('A'))



n,m=map(int,input().split())
list_one=[]
list_chess=[]
for i in range(n):
    list_one=str(input())
    list_chess.append(list_one)

repaint_chess(list_chess,n,m) 
