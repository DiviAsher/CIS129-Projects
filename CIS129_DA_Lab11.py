
# CIS129 - Module 11 Lab: Grade file storage
# Divinity Asher
# 04/26/2024
# This program allows the user to enter grades into a text file.

# Main function
def main():
    print()
    with open('grades.txt', mode='w') as grades:
        gradeInput = grades.write(input("Please enter the grades from the class, use -1 to end the program: "))
    
    while gradeInput != -1:
        

# Call to main
main()
