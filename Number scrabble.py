print(" \t \t \t**the point from this game** \n")
print("If a player has picked three numbers =15, that player wins the game.")

player1=input("player1 please enter your name : \n")
player2=input("player2 please enter your name : \n")

list=[1,2,3,4,5,6,7,8,9]
p1=[]
p2=[]

print("\nlist=[1,2,3,4,5,6,7,8,9]")
while( 1 ):
    x=int(input(player1 + " please enter which number u want from the list ""\n"))
    while ((x in p1) or (x in p2) or( x==0) or (x>9)):
        print("\nError, it is not in the list,\n please",player1 ,"choose  which number you want from  this list \n",list)
        print("you have now",p1,"\n""and",player2,"have",p2)
        x=int(input("so which number will close you to your point:\n"))
        
    p1.append(x)
    list[x-1]=0          
    print('\n',player1,"have now",p1)
    print(player2,"have now",p2)                       
    if (list==[0,0,0,0,0,0,0,0,0]):
        break
    else:
        print(list)
        y=int(input(player2 +" please enter which number u want from the list""\n"))
        while ((y in p1) or (y in p2) or( y==0) or (y>9)):
            print("\nError, it is not in the list, \n please",player2 ,"choose  which number you want from  this list \n",list)
            print("you have now",p2,"\n""and",player1,"have",p1)
            y=int(input("so which number will close you to your point:\n"))

                                                    
        list[y-1]=0
        p2.append(y)
        print("\nlist=",list)
        print(player1,"have now",p1)
        print(player2,"have now",p2)
sum1=0
sum2=0
for x,y in enumerate(p1):
    for n,m in enumerate(p1):
        for t,u in enumerate(p1):
            if(y+m+u==15):
                sum1=15
                
for x,y in enumerate(p2):
    for n,m in enumerate(p2):
        for t,u in enumerate(p2):
            if(y+m+u==15):
                sum2=15
                
if((sum1!=15 and sum2!=15) or (sum1==15 and sum2==15)):
    print("draw")
elif(sum2==15):
    print(player2,"won \n")
elif(sum1==15):
    print(player1,"won \n" )

end=int(input("if you like to end the program please enter 0 \n"))
while(end!=0):
    end=int(input("if you like to end the program please enter 0 \n"))

    
    
