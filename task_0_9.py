
def vowels(string):
    
    for character in string:
        if character in "aeiou":
            print(character, end=', ')
    return character,lower()
string = "Umuzi"

vowels(string)
