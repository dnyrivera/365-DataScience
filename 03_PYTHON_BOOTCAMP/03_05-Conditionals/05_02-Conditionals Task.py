"""
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
"""
# user_number = int(input("Enter the number between 1-5: "))
# if user_number == 1:
#     print(f"One - {user_number}")
# elif user_number == 2:
#     print(f"Two - {user_number}")
# elif user_number == 3:
#     print(f"Three - {user_number}")
# elif user_number == 4:
#     print(f"Four - {user_number}")
# elif user_number == 5:
#     print(f"Five - {user_number}")
# else:
#     print(f"{user_number} that isn't a number in the range")

"""
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
"""
# user_number = input("Enter the string of the number between 1-5: ").lower()
# # user_number.lower()
# if user_number == "one":
#     print(f"1 - {user_number}")
# elif user_number == "two":
#     print(f"2 - {user_number}")
# elif user_number == "three":
#     print(f"3 - {user_number}")
# elif user_number == "four":
#     print(f"4 - {user_number}")
# elif user_number == "five":
#     print(f"5 - {user_number}")
# else:
#     print(f"{user_number} that isn't a number in the range")

"""
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
"""
# secret_number = 7
# guess = input("Guess the number between 1-10 : ")

# if guess.isdigit():
#     guess = int(guess)

#     if guess == secret_number:
#         print("You guessed the correct number! You win!")
#     elif guess > secret_number and guess <= 10:
#         print("You guessed too high number! Sorry you lose!")
#     elif guess < secret_number and guess >= 1:
#         print("You guessed too low number! Sorry you lose!")
#     else:
#         print("Out of Range")
# else:
#     print("That's not even an integer! What are you playing at?!")


"""
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
"""
user_name = input("Input your name : ")

if len(user_name) >= 5:
    print(f"Your name contains {len(user_name)} characters ")
else:
    print("I'm not telling you the length of your name")


"""
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
"""


"""
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
"""
