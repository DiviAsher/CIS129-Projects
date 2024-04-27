
# CIS129 - Module 11 Lab: Class Average Program
# Divinity Asher
# 04/26/2024
# This program allows the user to enter grades into a text file.

# Write function
def writeText():
    print()
    inputList = []
    
    userInput = input("Please enter the grades from the class, type 'done' to end the program: ")

    while userInput.lower() != 'done':
        inputList.append(userInput)
        userInput = input("Enter another grade, 'done' to end: ")

    print("Recorded Grades:", inputList)

# Call to write the grades in the text file.
writeText()
