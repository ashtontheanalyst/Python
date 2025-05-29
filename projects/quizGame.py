# Quiz game
# Practicing lists, 2D lists, tuples, etc.

questions = ("Is the sky blue?", 
             "In what year was Python released?", 
             "Who is the President? ")

options = (("Yes", "No"), 
           ("1986", "2013", "1991", "2004"), 
           ("Taylor Swift", "Donald Trump", "Jack Black", "George Strait"))

answers = ("Yes", "1991", "Donald Trump")
guesses = []

score = 0

print("-------------------- QUIZ GAME --------------------")
for i in range(len(questions)):
    print(questions[i])
    
    print(f"Options: ", end="")
    for j in range(len(options[i])):
        print(f"'{options[i][j]}'", end=" ")
    print()

    guess = input("Guess: ")
    guesses.append(guess)

    if guesses[i].lower() == answers[i].lower():
        print("CORRECT!")
        print()
        score += 1
    else:
        print("INCORRECT!!!")
        print(f"{answers[i]} was the correct answer")
        print()

print("--------------------- RESULTS ---------------------")
print(f"Your score was {score} out of {len(answers)}!")
print("---------------------------------------------------")