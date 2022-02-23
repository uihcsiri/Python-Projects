#Rock, Paper, Scissors, Lizard, Spock, Cloth
print("Welcome to play \"Rock, Paper, Scissors, Lizard, Spock\"")

instruction1 = """Please see below for the rule:
    Scissors cuts paper.
    Paper covers rock.
    Rock crushes lizard.
    Lizard poisons Spock.
    Spock smashes scissors.
    Scissors decapitates lizard.
    Lizard eats paper.
    Paper disproves Spock.
    Spock vaporizes rock.
    Rock crushes scissors."""
print(instruction1)

print("\nPlease choose your weapon!")
instruction2 = """Please see below for what each number stands for:
    1: Rock
    2: Paper
    3: Scissors
    4: Lizard
    5: Spock"""
print(instruction2)
print("Enter a number between 1 and 5!")


#code starts from here
weap_dict = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
    4: "Lizard",
    5: "Spock",
}

def fight(user): #return T/F
 import random
 competitor = random.randint(1,5)
 print("The computer chooses \""+ weap_dict [competitor]+"\"")
 again = True
 if (user == 1): 
     if (competitor == 4 or competitor==3):
         print("You win!")
         again = play_again()
     elif (competitor == 2 or competitor==5):
         print("You lose!")
         again = play_again()
     else:
         print("Draw")
         again = play_again()
 if (user == 2): 
     if (competitor == 1 or competitor==5):
         print("You win!")
         again = play_again()
     elif (competitor == 3 or competitor==4):
         print("You lose!")
         again = play_again()
     else:
         print("Draw")
         again = play_again()
 if (user == 3): 
     if (competitor == 2 or competitor==4):
         print("You win!")
         again = play_again()
     elif (competitor == 1 or competitor==5):
         print("You lose!")
         again = play_again()
     else:
         print("Draw")
         again = play_again()
 if (user == 4): 
     if (competitor == 2 or competitor==5):
         print("You win!")
         again = play_again()
     elif (competitor == 1 or competitor==3):
         print("You lose!")
         again = play_again()
     else:
         print("Draw")
         again = play_again()
 if (user == 5): 
     if (competitor == 3 or competitor==1):
         print("You win!")
         again = play_again()
     elif (competitor == 2 or competitor==4):
         print("You lose!")
         again = play_again()
     else:
         print("Draw")
         again = play_again()
 return again

""" just for your reference 
1 beats 4 & 3
2 beats 1 & 5
3 beats 2 & 4
4 beats 2 & 5
5 beats 3 & 1
"""



def play_again():
    flag_again = 1
    while flag_again > 0:
        print("Would you like to play again?")
        print("Please just key \"Y\" or \"N\"")
        try: 
            answer = input()
            if (answer=="Y" or answer == "y"):
                flag_again-=1
                print("\nPlease choose your weapon!")
                return True
            elif (answer=="N" or answer =="n"):
                flag_again-=1
                print("Game over")
                return False
            else:
                raise ValueError

        except(TypeError, ValueError):
            print("Only \"Y\" or \"N\" are allowed.")
            print("Please try again.\n")

while True: 
 try: 
     user = int(input())
     print ("You choose \"" + weap_dict[user]+"\"")
     start_again = fight(user)
     print('[DEBUG]', start_again)
     if start_again == False:#但他好像停不下來QQ
         print("I said stop")
         break
    
 except (TypeError, ValueError, KeyError):
     print("Please enter numbers between 1 and 6.") 
     #keyerror happens when using dict==>有辦法在user input時就偵測到嗎?

