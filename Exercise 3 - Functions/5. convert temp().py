def convert_to_celcius(Tf):
    Tc = 5/9*(Tf-32)
    return Tc


def convert_to_kelvin(Tc):
    Tk = Tc+273.15
    return Tk


def convert_temp():
    Tf = int(input("Enter a temperature in Fahrenheit: "))
    Tc = convert_to_celcius(Tf)
    Tk = convert_to_kelvin(Tc)
    print('\n')
    print("The temperature in Fahrenheit is:", Tf)
    print("The temperature in Celcius is:", Tc)
    print("The temperature in Kelvin is:", Tk)

