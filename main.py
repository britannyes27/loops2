# print("hello world")
# #print is a function that prints out a message to the console
# #strings are surrounded by quotes
# #single or double quotes " or ""
# #whenever a word is surrounded by quotes it is called a string 
# #be consistent with the quotes you use
# print("your name")
# print("order of execution")
# print("in python")
# print("*"*20)
# #variables are used to store data
# #variables are created when you assign a value to it
# #variables are case sensitive
# price = 10 #integer variable
# name = "John" #string variable
# rating = 4.9 #float variable
# is_published = True #boolean variable
# #start all variables with a lowercase letter or underscore
# print(name)
# print(price)
# print(rating)
# print(is_published)
# #string interpolation where you can use variables in a sentence
# print(name + " is a basketball player")
# # concatenation to join variables in a sentence using # the plus (+) sign
# print(name + " has a rating of " + str(rating))
# #use the str() function to convert a number to a string
# # this is called type conversion
# print("the price of the book is " + str(price))
# # getting input from the user

# name = input("What is your name?")
# age = input("What is your age?")
# occupation = input("What is your occupation?")
# print("Hello " + name + " you are " + age + " years old and you are a " + occupation)


averagegrade = input("What is your average grade? ")
numberextracurricular = input("How many extra curriculars? ")
awardacademic = input("What rewards have you earned? ")
votes = int(input("voters"))
recognitions = input("What recognitions do you have? ")

if averagegrade >= 85:
    print("honor roll")

if numberextracurricular > 3:
    print("high involvement")

print("categories are most likely to succeed. class artist")
