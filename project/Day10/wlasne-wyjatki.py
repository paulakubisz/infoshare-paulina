class TooColdException(Exception):

    def __init__(self, temp):
        super().__init__(f"Temperature {temp} is below absolute 0")


def celcius_to_kelvin(temp):
    if temp < -273.15:
        raise TooColdException(temp)
    return temp * 273.15

print(celcius_to_kelvin(-2223))
print(celcius_to_kelvin(23))
print(celcius_to_kelvin(-123))
print(celcius_to_kelvin(0))





print("========drugie rozwiazanie=====")

try:
    print(celcius_to_kelvin(-2223))

except TooColdException:
    print("Zbyt zimno")