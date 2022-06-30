#!/usr/bin/env python3

# what anime character are you

# this will be the beginning of the sentence to the end of the game
# must print this at the end


from time import sleep

# need something to hold the values of message

message = ""

animeAnswer = "You totally remind me of "


# need key and values for question 1 and points

questionAnswers = {"question 1": "c", "question 2": "a", "question 3": "d", "question 4": "a",
                   "question 5": "c", "question 6": "a", "question 7": "b", "question 8": "c", "question 9": "Yes"}

print("ARE YOU THE GREATEST SHONEN ANIME EVER? \n Let's Find Out!")
sleep(.5)
print("I will ask you a series of questions to see if you could be me in a fight\n but first we have to see who you are")
sleep(2)
print("Are you ready?\n LETS BEGIN!")
sleep(2)


# from a total of 10 questions I need to add the total up and get a percentage

#total = (int(question1) + int (question2) + int(question3) + int (question4) + int(question5) + int (question6) + int(question7) + int (question8) + int(question9) + int (question10))
question1 = input(
    "In Naruto, who does Naruto fight in the Chunin Exam finals?\n (a) Sasuke \n (b) Hinata \n (c) Neji \n (d) Orochimaru ")

question1 = question1.lower()

if question1 == "c":
    message = "Great! Let's Continue"
elif question1 == "a":
    message = "Okay... Let's Continue"
elif question1 == "b":
    message = "Alright... Let's Continue"
elif question1 == "d":
    message = "Good! Let's Continue"
else:
    message = "Please enter in A or B or C or D and try again"

print(message)
sleep(2)

question2 = input(
    "In Bleach, Rukia goes back to Ichigo's world to help Ichigo and the others? \n (a) True \n (b) False ")
question2 = question2.lower()

if question2 == "a":
    message = "Great! Let's Continue"
elif question2 == "b":
    message = "Good! Let's Continue"
else:
    message = "Please enter in A or B and try again"

print(message)
sleep(2)

question3 = input(
    "In Dragon Ball Z, who fights Cell after Goku gives up?\n (a) Piccolo \n (b) Cell Jr. \n (c) Vegeta \n (d) Gohan ")
question3 = question3.lower()
if question3 == "d":
    message = "Great! Let's Continue"
elif question3 == "a":
    message = "Okay... Let's Continue"
elif question3 == "b":
    message = "Alright... Let's Continue"
elif question3 == "c":
    message = "Good! Let's Continue"
else:
    message = "Please enter in A or B or C or D and try again"

print(message)
sleep(2)

question4 = input(
    "Does the manga, Bobobo-bobo-bobo, appear in Shonen Jump?\n (a) Yes \n (b) No ")
question4.lower()
if question4 == "a":
    message = "Great! Let's Continue"
elif question4 == "b":
    message = "Good! Let's Continue"
else:
    message = "Please enter in A or B and try again"

print(message)
sleep(2)

question5 = input(
    'In the video game, Naruto Ultimate Ninja, how many characters are there? \n (a) 75 \n (b) 60 \n (c) 100 \n (d) 55 ')
question5 = question5.lower()
if question5 == "c":
    message = "Great! Let's Continue"
elif question5 == "a":
    message = "Okay... Let's Continue"
elif question5 == "b":
    message = "Alright... Let's Continue"
elif question5 == "d":
    message = "Good! Let's Continue"
else:
    message = "Please enter in A or B or C or D and try again"

print(message)
sleep(2)

question6 = input(
    "How does Sasuke make Gaara bleed in Naruto? \n (a) Chidori \n (b) Shadow Clone Jutsu \n (c) Rasengan \n (d) Demon Wind bomb ")
question6 = question6.lower()
if question6 == "a":
    message = "Great! Let's Continue"
elif question6 == "c":
    message = "Okay... Let's Continue"
elif question6 == "b":
    message = "Alright... Let's Continue"
elif question6 == "d":
    message = "Good! Let's Continue"
else:
    message = "Please enter in A or B or C or D and try again"

print(message)
sleep(2)

question7 = input(
    "Was Shonen Jump made in America in 2008?\n (a) True \n (b) False ")
question7 = question7.lower()
if question7 == "a":
    message = "Great! Let's Continue"
elif question7 == "b":
    message = "Good! Let's Continue"
else:
    message = "Please enter in A or B and try again"

print(message)
sleep(2)

question8 = input(
    "In Yu-Gi-Oh GX, what color is Jaden's shirt? \n (a) Tie-dye \n (b) Black \n (c) Red \n (d) Green ")
question8 = question8.lower()
if question8 == "c":
    message = "Great! Let's Continue"
elif question8 == "b":
    message = "Okay... Let's Continue"
elif question8 == "a":
    message = "Alright... Let's Continue"
elif question8 == "d":
    message = "Good! Let's Continue"
else:
    message = "Please enter in A or B or C or D and try again"

print(message)
sleep(2)

question9 = input("Is Naruto 13 years old? \n (a) Yes \n (b) No ")
question9 = question9.lower()
if question9 == "a":
    message = "Great! Let's Continue"
elif question9 == "b":
    message = "Good! Let's Continue"
else:
    message = "Please enter in A or B and try again"

print(message)


sleep(1)
print("hold on let me think of a question... Because you need a bonus question... Sheesh these Scores are terrible \n I'll even give you three tries.\n ready? ")
sleep(3)

round = 0
question10 = ""

while round < 3 and (question10 != "naruto" and question10 != "saitama"):
    round += 1     # increase the round counter by 1
    question10 = input(
        'What Has been the greatest final fights in Anime History \n (levi) Levi Vs. The Beast Titan \n (naruto) Naruto Vs Sasuke \n (edward)Edward Elric Vs Father \n (spike)Spike Vs Vicious \n (goku) Goku vs Kid Buu \n(yusuke) Yusuke Vs Yomi \n (JUST USE THE FIRST NAME OF THE FIGHTS!) \n\n ')
    question10 = question10.lower()  # this line inserted to line 8 will make all
    # user input starts with an uppercase
    if question10 == "naruto":  # logic to check if user gave correct answer
        print("Correct!")
    elif question10 == "saitama":
        print("You gave the super secret answer!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Naruto Vs Sasuke.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")


sleep(2)

print("Now Lets go over the scores")


print("for question 1 you answered " + question1 +
      " and the answer was " + questionAnswers["question 1"])
sleep(1.5)
print("for question 2 you answered " + question2 +
      " and the answer was " + questionAnswers["question 2"])
sleep(1.5)
print("for question 3 you answered " + question3 +
      " and the answer was " + questionAnswers["question 3"])
sleep(1.5)
print("for question 4 you answered " + question4 +
      " and the answer was " + questionAnswers["question 4"])
sleep(1.5)
print("for question 5 you answered " + question5 +
      " and the answer was " + questionAnswers["question 5"])
sleep(1.5)
print("for question 6 you answered " + question6 +
      " and the answer was " + questionAnswers["question 6"])
sleep(1.5)
print("for question 7 you answered " + question7 +
      " and the answer was " + questionAnswers["question 7"])
sleep(1.5)
print("for question 8 you answered " + question8 +
      " and the answer was " + questionAnswers["question 8"])
sleep(1.5)
print("for question 9 you answered " + question9 +
      " and the answer was " + questionAnswers["question 9"])
sleep(1.5)


print("Now Lets calculate the scores.....")
sleep(5)

