# function to coverts degrees celsius to degrees fahrenheit

def convert_cel_to_fah(C):
    F = C * (9/5) + 32
    return F

# function to convert degrees fahrenheit to degrees celsius

def convert_fah_to_cel(F):
    C = F - 32 * (5/9)
    return C
# converts celsius to fahrenheit
C = float(input("Enter temperature in degrees Celsius: "))

F = convert_cel_to_fah(C)

print(f"{C} degrees Celsius = {F} degrees Fahrenheit")

# convets fahrenheit to celsius
F = float( input("Enter temperature in degrees Fahrenheit: "))

C = convert_fah_to_cel(F)

print(f"{F} degrees fahrenheit = {C} degrees Celsius")
