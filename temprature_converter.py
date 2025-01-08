# Utilities
def input_number(unit):
    a=input(f"Enter a number to convert from celsius to {unit}: ")
    return a


def print_output(input, input_num, output, output_number):
    print("=================================")
    print(f"     {input_num} {input} == {output_number} {output}")
    print("=================================")
#conversion from celsius to unit

def celsius_to_kelvin():
    celsius = input_number("kelvin")

    kelvin = (int(celsius) + 273.15)

    print_output("celsius", celsius, "kelvin", kelvin,)

def celsius_to_farenheit():
    celsius = input_number("farenheit")

    farenheit = (int(celsius)  *9/5 + 32 )

    print_output("celsius", celsius, "farenheit", farenheit)
#main call
def temprature_conversion():
    a = input("select conversion option : ")
    if a== "0":
        print("welcome to celsius to kelvin")
        celsius_to_kelvin()
    elif a== "1":
        print("welcome to celsius to farenheit")
        celsius_to_farenheit()
    else :
        print("match not found")
