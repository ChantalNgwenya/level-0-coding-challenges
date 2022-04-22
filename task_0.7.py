

def celsius_to_fahrenheit(Celsius):
    Fahrenheit = Celsius * (9/5) + 32
    return Fahrenheit

def fahrenheit_to_celsius(Fahrenheit):
    Celsius = Fahrenheit - 32 * (5/9)
    return Celsius

Celsius = 100

Fahrenheit = celsius_to_fahrenheit(Celsius)

print(f"{Celsius} degrees Celsius = {Fahrenheit} degrees Fahrenheit")


Fahrenheit = 200

Celsius = fahrenheit_to_celsius(Fahrenheit)

print(f"{Fahrenheit} degrees fahrenheit = {Celsius} degrees Celsius")
