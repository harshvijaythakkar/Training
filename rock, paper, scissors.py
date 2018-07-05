#rock, paper, scissors game
from random import randint as r

total_game = 0
user_won = 0
computer_won = 0
user_lose = 0
computer_lose = 0
draw = 0
choice = 'y'

while choice == 'y':
    total_game += 1
        
    computer_choices = {1:"rock", 2:"paper", 3:"scissors"}

    user_choices = {1:"rock", 2:"paper", 3:"scissors"}

    computer_choice_index = r(1,3)

    #print (computer_choices[computer_choice_index])
    print ("\nLet's play \"ROCK, PAPER & SCISSORS\" GAME\n")
    print ("3....2....1....\n")
    print ("Computer:guess from the following.")
    
    try:
        user_choice_index = int(input("1.rock\n2.paper\n3.scissors\n\nEnter number between 1 - 3:"))
        if user_choice_index <= 3:
                
            print ("\n" + computer_choices[computer_choice_index] + " vs. " + user_choices[user_choice_index] + "(You)")

            if (computer_choices[computer_choice_index] == user_choices[user_choice_index]):
                print ("You tied! That will not work!\nComputer: it's a tie!")
                draw += 1

            elif (computer_choices[computer_choice_index] == "rock" and user_choices[user_choice_index] == "paper"):
                print ("You won!\nComputer: You win this time. Try me again if you aren't afraid to lose!")
                user_won += 1
                computer_lose += 1

            elif (computer_choices[computer_choice_index] == "rock" and user_choices[user_choice_index] == "scissors"):
                print ("You lost!\nComputer: i knew you couldn't do it. Feel free to keep trying.")
                user_lose += 1
                computer_won += 1
            
            elif (computer_choices[computer_choice_index] == "scissors" and user_choices[user_choice_index] == "rock"):
                print ("You won!\nComputer: You won? Ahhh! well, perhaps you are better then you appear.")
                user_won += 1
                computer_lose += 1
                
            elif (computer_choices[computer_choice_index] == "scissors" and user_choices[user_choice_index] == "paper"):
                print ("You lost!\nComputer: ha! you lose! Better luck next time")
                user_lose += 1
                computer_won += 1
            
            elif (computer_choices[computer_choice_index] == "paper" and user_choices[user_choice_index] == "scissors"):
                print ("You won!\nComputer: hmmph! it was luck! You shall not beat me again, i daresay")
                user_won += 1
                computer_lose += 1
                
            elif (computer_choices[computer_choice_index] == "paper" and user_choices[user_choice_index] == "rock"):
                print ("You lost!\nComputer: Did you really think you could beat me?")
                user_lose += 1 
                computer_won += 1

            else:
                pass
            
    except Exception as e:
        print("Computer: You are disqualified! next time input a proper choice.\n")
        break
           
    choice = input("Do you want to play again?[y/n]").lower()
    if choice == 'y':
        continue
    else:
        print("I think you dont want to continue.")
        break

print ("\nRESULT:-\n")
#print ("TOTAL NO OF GAMES:", total_game)
print ("\twon\tlose\tdraw\ttotal\n")
print ("User\t", user_won, "\t", user_lose, "\t", draw, "\t", total_game)
print ("Comp\t", computer_won, "\t", computer_lose, "\t", draw, "\t", total_game)

if user_won > computer_won:
    print ("Congratulation!, You won the game")
    print ("Computer: oh!, This time you won. Well played.")
elif user_won == computer_won:
    print ("Computer: It's draw! Well played, but u can't beat me.Try it next time.")
else:
    print ("Computer: Yeh! I won the game. No one can beat me. Try it next time")

input()

