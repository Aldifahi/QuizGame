print("Welcome to Ali's Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()



print("Okayy! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("who is the first president of the united states? ")
if answer.lower() == ("george washington"):
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does “www” stand for in a website browser?")
if answer.lower() == "world wide web":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")