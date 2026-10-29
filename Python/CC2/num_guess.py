secret = 7
 
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret: # 3 == 7 ? F
        print("Correct! You win!")
        break
    elif guess < secret: # 3 < 7 ? T
        print("Too low, try again")
    else:
        print("Too high, try again")
