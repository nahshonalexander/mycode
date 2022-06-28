#!/usr/bin/env python3


wordbank= ["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]


wordbank.append(4)

num = int(input("What is a number between 0-18"))
choice = int(input("Pick a student number"))
student_name = tlgstudents[choice]
realNum = print(str(num))


print(f"{student_name} always uses {wordbank[2]} to indent ")
