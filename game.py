player1=input("Enter First Player's Name : ")
player2=input("Enter Second Player's Name : ")

print("Hello "+player1+" and "+player2+"!")
print("This is rock, paper, scissors game!")

chance=0
ps1=0
ps2=0
p1=''
p2=''

while chance!=3:
    round=chance+1
    print("================   ROUND = "+str(round)+"   ================")
    while p1 != 'r' or p1 != 'p' or p1 != 's':
        print(player1 + ", Please Choose any one of the following three..")
        p1 = input("r for rock, p for paper, s for scissors : ")
        if p1 == 'r' or p1 == 'p' or p1 == 's':
            break
    print(player1 + ", now hide your answer, and ask " + player2 + " to choose his/her option!")

    while p2 != 'r' or p2 != 'p' or p2 != 's':
        print("\n" + player2 + ", Choose any one of the following three..")
        p2 = input("r for rock, p for paper, s for scissors : ")
        if p2 == 'r' or p2 == 'p' or p2 == 's':
            break


    if(p1=='r' and p2=='s' or p1=='p' and p2=='r' or p1=='s' and p2=='p'):
        print("\n  *******  "+player1+" won "+str(round)+"!  *******\n")

        chance+=1
        ps1+=1


    if (p2 == 'r' and p1 == 's' or p2 == 'p' and p1 == 'r' or p2 == 's' and p1 == 'p'):
        print("\n  *******  "+player2+" won "+str(round)+"!  *******\n")
        chance+=1
        ps2+=1

    if (p2 == 'r' and p1 == 'r' or p2 == 'p' and p1 == 'p' or p2 == 's' and p1 == 's'):
        print("\n  **********  This round was a tie!!  **********  \n")

if(ps1>ps2):
    print("\n\n========  "+player1.upper() + " WON THE MATCH  ========")

else:
    print("\n\n========  "+player2.upper() + " WON THE MATCH  ========")

