

def celsius_to_fahrenheit(Celsius):
    Fahrenheit = Celsius * (9/5) + 32
    return print(f"{Celsius} degrees Celsius = {Fahrenheit} degrees Fahrenheit")


def fahrenheit_to_celsius(Fahrenheit):
    Celsius = Fahrenheit - 32 * (5/9)
    return print(f"{Fahrenheit} degrees fahrenheit = {Celsius} degrees Celsius")

celsius_to_fahrenheit(100)

fahrenheit_to_celsius(200)

