# Functon takes in a string and prints out the vowels
def vowels(string):
    # to print the vowels
    for char in string.lower():
        if char in "aeiou":
            print(char, end=', ')
    return char

# take input
string = input('Enter any string: ')

# calling function
vowels(string)
