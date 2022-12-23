# Lets make a quiz.

name = input("Hello, Welcome to my Quiz!" + "\nWhat's your name? ")

print(name)

start = input("Hello " + name + ", do you want to start? ")
if start.lower() != "yes":
    quit()

print("Alright, let's begin.")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("All Done.")

print("You got " + str(score) + " correct.")
print("You got " + str((score/3) * 100) + "% correct.")