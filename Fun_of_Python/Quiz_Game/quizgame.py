print("Welcome to my The Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Goodbye!")
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("what does HGP stand for? ")
if  answer.lower() == "hidden genius project":
    print("Correct")
    score += 1 # or score = score + 1
else: 
    print("Incorrect")


answer = input("What does U.S.A stand for? ")
if  answer.lower() == "united states of america":
    print("Correct")
    score += 1
else: 
    print("Incorrect")


answer = input("What is the name of the creator? ").lower()
if  answer == "artisan jenkins":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

print(f"You got {score} question(s) correct!")
print(f"You got {score/3*100}%.")