def Kelvin2Fahrenheit(degree):
    assert(degree >= 0), "Can't be less than the zero"
    return ((degree-273)*1.8)+32


if __name__ == "__main__":
	print(Kelvin2Fahrenheit(273))
	print(Kelvin2Fahrenheit(10))
	print(Kelvin2Fahrenheit(0))
	print(Kelvin2Fahrenheit(-5))