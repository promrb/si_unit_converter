# utlities
def input_number(unit):
    a=input(f"Enter a number to convert from kg to {unit}: ")
    return a

def print_output(input, input_num, output, output_number):
    print("=================================")
    print(f"     {input_num} {input} == {output_number} {output}")
    print("=================================")


# conversion from kg to unit
def kg_to_gram():
    kg = input_number("gram")

    gram = (int(kg) * 1000)

    print_output("kg", kg, "gram", gram,)

def kg_to_milligram():
    kg = input_number("milligram")

    milligram = (int(kg) * 1000000)

    print_output("kg", kg, "milligram", milligram,)

def kg_to_metricton():
    kg = input_number("metricton")

    metricton = (int(kg) / 1000)

    print_output("kg", kg, "metricton", metricton,)

def kg_to_longton():
    kg = input_number("longton")

    longton = (int (kg) * 0.000984)

    print_output("kg", kg, "longton", longton)

def kg_to_shortton():
        kg = input_number("shortton")

        shortton = (int(kg) / 907.2)

        print_output("kg", kg, "shortton", shortton,)

def kg_to_pound():
    kg = input_number("pound")

    pound = (int(kg) * 2.205)

    print_output("kg", kg, "pound", pound,)

def kg_to_ounce():
    kg = input_number("ounce")

    ounce = (int(kg) * 35.274)

    print_output("kg", kg, "ounce", ounce)

def kg_to_carat():
    kg = input_number("carat")

    carat = (int(kg)* 5000)

    print_output("kg", kg, "carat", carat)

def kg_to_atomicmassunit():
    kg = input_number("atomic mass unit")

    atomicmassunit = (float(kg) * (6.022*10e26))

    
    print_output("kg", kg, "atomicmassunit", atomicmassunit,)
#main call
def mass_conversion():
    a = input("select conversion option:")
    if a=="0":
        print ("welcome to kg to gram")
        kg_to_gram()
    elif a == "1":
        print("welcome to kg to milligram")
        kg_to_milligram()
    elif a == "2":
        print("welcome to kg to metric_ton")
        kg_to_metricton()
    elif a== "3":
        print("welcome to kg to longton")
        kg_to_longton()
    elif a== "4":
        print("welcome to kg to shortton")
        kg_to_shortton()
    elif a == "5":
        print("welcome to kg to pound")
        kg_to_pound()
    elif a== "6":
        print("welcome to kg to ounce")
        kg_to_ounce()
    elif a== "7":
       print("welcome to kg to carat")
       kg_to_carat() 
    elif a== "8":
        print("welcome to kg to atomic mass unit")
        kg_to_atomicmassunit()
    else:
        print("Match not found")
