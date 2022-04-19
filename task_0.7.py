

def celsius_to_fahrenheit(C):
    F = C * (9/5) + 32
    return F

def fahrenheut_to_celsius(F):
    C = F - 32 * (5/9)
    return C

C = float(input("Enter temperature in degrees Celsius: "))

F = celsius_to_fahrenheit(C)

print(f"{C} degrees Celsius = {F} degrees Fahrenheit")


F = float( input("Enter temperature in degrees Fahrenheit: "))

C = fahrenheit_to_celsius(F)

print(f"{F} degrees fahrenheit = {C} degrees Celsius")
