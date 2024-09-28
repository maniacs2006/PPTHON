import random 
num_rounds = 5
score = 0
print("Welcome to the High-Low Game!")
for round_num in range(1,num_rounds + 1):
    print(f"Round Number {round_num}")
    while True:
        try:
            player_num = int(input("Your number (should be between 1 and 100): "))
            if 1 <= player_num <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    comp_num = random.randint(1,100)
    print(f"Your number is: {player_num}")
    guess = input("Do you think your number is higher of lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()
    if (guess == "higher" and player_num > comp_num) or (guess == "lower" and player_num < comp_num):
        print(f"You were right! The computer's number was {comp_num}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {comp_num}")
    print(f"Your score is now {score}")

    print()

print("Thanks for playing!")
if score == num_rounds:
    print("Wow!, you've played perfectly!")
elif score >= num_rounds // 2 :
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
    