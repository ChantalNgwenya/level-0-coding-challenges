

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    print(f"{celsius} degrees Celsius = {fahrenheit} degrees Fahrenheit")


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} degrees Fahrenheit = {celsius} degrees Celsius")

celsius_to_fahrenheit(100)

fahrenheit_to_celsius(200)

