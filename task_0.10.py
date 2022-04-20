
def common_letters():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    s1 = set(string1.lower())
    s2= set(string2.lower())
    lst = s1 & s2
    print (lst)

common_letters()    
