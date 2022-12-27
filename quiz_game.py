print("*****Welcome to Computer Quiz*****")

playing = input("Do you want to play?  ")

# converting input to lower
if playing.lower() != "yes":
    quit()

print("Okay! Lets Play :)")

# initiiaze score to 0
score = 0

# question 1
answer = input("What does CPU stand for ?  ")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# question 2
answer = input("What does GPU stands for ?  ")

if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# question 3
answer = input("What does is stands for IP  ?  ")

if answer.lower() == "Internet Protocol":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# print score
print("You Score is! := " ,score)
print("You Got :" ,(score/2)*100 ,"%")