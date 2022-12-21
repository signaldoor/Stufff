name = input("Hello! Welcome to our game! \nWhats your name? ")

print(name)

play = input("\nHello " + name + ", Do you want to start? ")
if play.lower() != "yes":
    quit()

print("\nOkay, let's start!")

score = 0

answer = input("\nWhats the square root of 25? ")
if answer == "5":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("\nWhats the square root of 16? ")
if answer == "4":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("\nWhats 20 - 13? ")
if answer == "7":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("\nYou finished!!!")

print("\nYou got " + str(score) + " correct!")
print("You got " + str((score/3) * 100) + "% correct!")

