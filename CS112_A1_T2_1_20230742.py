# File: CS112_A1_T2_1_20230742
# Purpose: 100 game. Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# Author: Ahmed Ali
# ID: 20230742


print("\n****************************************")
print("welcome to the 100 game")
print("Two players start from 0 and alternatively add a number from 1 to 10 to the sum, the player who reaches 100 wins.")

#Start countimg from 0
sum = 0

while(sum < 100) :
    print("\n****************************************")
    print("\n")
    print("The total now is " , sum)
    p1 = input("Player one : Enter a number from 1 to 10: ")
#Ask player 1 to enter a number 
    while (p1 not in ['1','2','3','4','5','6','7','8','9',"10"]):
        p1 = input("This number is invalid please enter a valid number: ")

    sum += int(p1)
#Announce if player wins or draw    
    if (sum == 100):
        print("\n****************************************")
        print("Player one wins")
        break
    elif (sum > 100):
        print("\n****************************************")
        print ("Draw")
        break


    print("\n****************************************")
    print("\n")
    print("The total now is " , sum)
    p2 = input("Player two : Enter a number from 1 to 10: ")
#Ask player 2 to enter a number 
    while (p2 not in ['1','2','3','4','5','6','7','8','9',"10"]):
        p2 = input("This number is invalid please enter a valid number: ")

    sum += int(p2)
#Announce if player wins or draw    
    if (sum == 100):
        print("\n****************************************")
        print("Player two wins")
        break
    elif (sum > 100):
        print("\n****************************************")
        print ("Draw")
        break
print("^^^^^^^^^^^^^^^^^")    
print("End  of the game")
print("^^^^^^^^^^^^^^^^^")    
    


