
# CIS129 - Module 10 Lab: Check Protection
# Divinity Asher
# 04/08/2024
# This program receives check amounts for electronic deposits while protecting the deposit amount by filling space with leading asterisks

# Main Function
def main():
    print()

    endProgram = 'no'

    # While loop to run the program again
    while endProgram == 'no':

        checkAmount = float(input('Please input the dollar amount on the check you'd like to electronically deposit: '))

        print(f'{checkAmount:.2f}')

