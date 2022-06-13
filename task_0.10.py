
def common_letters():
    string1 = "house"
    string2 = "computers"
    s1 = set(string1.lower())
    s2= set(string2.lower())
    letters = s1 & s2
    print (', '.join(letters))

common_letters()    
