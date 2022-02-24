import random 

answer = random.randint(1, 50)

print("Please guess a number between 1 and 50")


def playagain ():
    while True:
        print("Play again? If yes, enter \"y\"; if no, enter \"n\"")
        re_again = input().lower()
        if re_again == 'y':
            return 1
        
        elif re_again == 'n':
            print("Game over! Thanks for your time!")
            return 0
            
        else:
            print("Error! Only \"y\" and \"n\" are allowed!")
            continue

count = 0 
up_b = 50
lo_b = 1

while count >= 0: 
    user = input()
    count += 1
 
    try:
        user = int(user)
        if (user<1 or user >50):
            raise ValueError
         
        elif (user != answer):
            print("Wrong answer!")
         
            if user > answer:
                up_b = user
                print("The answer is between ", lo_b, " and ", up_b)
                print("Guess again!")
                continue
         
            else:
                lo_b = user
                print("The answer is between ", lo_b, " and ", up_b)
                print("Guess again!")
                continue

 
        elif (user == answer):
            print("Correct! Congratulation! You've guessed:", count, "times." )
            again = playagain()
            if again == 1:
                print("Please guess a number between 1 and 50")
                continue
            else: 
                break

    except(ValueError, TypeError):
        print("Error! Please enter an integer between 1 and 50")
        continue #go back to 10th line (correct!)