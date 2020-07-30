def jump_jump(distance, move_count, move, fibonacci):
    while True: 
        if distance>fibonacci:
            move_count+=1
            move+=1
            fibonacci+=move
            distance-=move
            
        elif distance==fibonacci:
            move_count+=1
            distance-=move
            fibonacci+=move
            if distance==0:
                print(move_count)
                break
        else:
            if move==1:
                move+=1
            move_count+=1
            move-=1
            fibonacci+=move
            distance-=move
            if distance==0:
                print(move_count)
                break
       
            

def Alpha_Cemtauri(x, y):
    distance=y-x-1
    move_count=1
    move=1
    fibonacci=1
    jump_jump(distance, move_count, move, fibonacci)

x,y=input().split()
x=int(x)
y=int(y)
distance=0
move_count=0

Alpha_Cemtauri(x, y)