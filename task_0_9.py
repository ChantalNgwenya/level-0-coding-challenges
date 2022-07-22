
def vowels(string):
    duplicated_vowels = ""
    vowels = ""

    for letter in string:
       if letter.lower() in "aeiou":
           duplicated_vowels = duplicated_vowels + str(letter.lower()) +" "
    
    
    for letter in duplicated_vowels:
        if letter not in vowels:
            vowels = vowels + letter +", "
    
    print(f"Vowels: " +{ vowels[:-2]}')
  
vowels('Umuzi')
