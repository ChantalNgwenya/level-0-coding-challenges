
def common_letters(string_1, string_2):
    s1 = set(string_1.lower())
    s2= set(string_2.lower())
    letters = s1 & s2
    print ('Common letters:',', '.join(letters))

common_letters("house", "computers")    
