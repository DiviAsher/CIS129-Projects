
# CIS129 - Module 11 Lab: Class Average Program
# Divinity Asher
# 04/26/2024
# This program allows the user to enter grades into a text file.

# Write function
def writeText():
    print()
    with open('grades.txt', mode='w') as grades:
        gradeInput = grades.write(input("Please enter the grades from the class, use -1 to end the program: "))
        close
    
    while gradeInput != "-1":
        with open('grades.txt', mode='w') as grades:
            gradeInput = grades.write(input("Enter grade, -1 to end: "))
        return gradeInput
        
# Call to write the grades in the text file.
writeText()

