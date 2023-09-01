# Unit Converter

def meters_to_feet(meters):
    return meters * 3.281

def centimeters_to_inches(centimeters):
    return centimeters * 0.393701

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kilogram_to_pounds(kilogram):
    return kilogram * 2.20462

def grams_to_ounces(grams):
    return grams * 0.03527396

def smeters_to_sfeet(square_meters):
    return square_meters * 10.764

def sfeet_to_smeters(square_feet):
    return square_feet / 10.764

def miles_to_kilometers(miles):
    return miles * 1.60934

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! please enter a valid number.")

def main():
    print("Unit Converter")
    print("-------------------------")
    print("1. Length Converter")
    print("2. Temperature Converter")
    print("3. Weight Converter")
    print("4. Area Converter")
    print("5. Speed Converter")
    print("-------------------------")

    choice = get_int_input("Enter your choice (1/5): ")
    
    if choice == 1:

        print("In category Length Converter")
        print("----------------------------------")
        print("1. Meters (m) to Feet (ft)")
        print("2. Centimeters (cm) to Inches (in)")
        print("3. Kilometers (km) to Miles (mi)")
        print("----------------------------------")
        category = get_int_input("Enter your choice (1/3): ")

        if category == 1:

            meters = get_float_input("Enter length in Meters: ")
            feet = meters_to_feet(meters)
            print(f"{meters} Meters is equal to {feet:.2f} feet.")
        
        elif category == 2:

            centimeters = get_float_input("Enter length in Centimeters: ")
            inches = centimeters_to_inches(centimeters)
            print(f"{centimeters} Centimeters is equal to {inches:.2f} inches.")
        
        elif category == 3:

            kilometers = get_float_input("Enter length in kilometers: ")
            miles = kilometers_to_miles(kilometers)
            print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

        else:
            print("Invalid choice. try again :( ")
            
    elif choice == 2:

        print("In category Temperature Converter")
        print("----------------------------------")
        print("1. Celsius (°C) to Fahrenheit (°F)")
        print("2. Celsius (°C) to Kelvin (K)")
        print("----------------------------------")
        category = get_int_input("Enter your choice (1/2): ")

        if category == 1:

            celsius = get_float_input("Enter Temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")

        elif category == 2:

            celsius = get_float_input("Enter Temperature in Celsius: ")
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius} Celsius is equal to {kelvin:.2f} Kelvin.")

        else: 
            print("Invalid choice. try again :( ")

    elif choice == 3:

        print("In category Weight Converter")
        print("--------------------------------")
        print("1. Kilograms (kg) to Pounds (lb)")
        print("2. Grams (g) to Ounces (oz)")
        print("--------------------------------")
        category = get_int_input("Enter your choice (1/2): ")

        if category == 1:

            kilogram = get_float_input("Enter Weight in Kilograms: ")
            pounds = kilogram_to_pounds(kilogram)
            print(f"{kilogram} kilogram is equal to {pounds:.2f} pounds.")

        elif category == 2:

            grams = get_float_input("Enter Weight in Grams: ")
            ounces = grams_to_ounces(grams)
            print(f"{grams} gram is equal to {ounces:.2f} ounce.")

        else: 
            print("Invalid choice. try again :( ")

    elif choice == 4:

        print("In category Area Converter")
        print("------------------------------------------")
        print("1. Square Meters (m²) to Square Feet (ft²)")
        print("2. Square Feet (ft²) to Square Meters (m²)")
        print("------------------------------------------")
        category = get_int_input("Enter your choice (1/2): ")

        if category == 1:

            square_meters = get_float_input("Enter Area in Square Meters (m²): ")
            square_feet = smeters_to_sfeet(square_meters)
            print(f"{square_meters} Square Meters (m²) is equal to {square_feet:.2f} Square Feet (ft²).")

        elif category == 2:

            square_feet = get_float_input("Enter Area in Square Feet (ft²): ")
            square_meters = sfeet_to_smeters(square_feet)
            print(f"{square_feet} square feet (ft²) is equal to {square_meters:.2f} square meters (m²).")

        else: 
            print("Invalid choice. try again :( ")

    elif choice == 5: 

        print("In category Speed Converter")
        print("-----------------------------------------------------")
        print("1. Kilometers per Hour (km/h) to Miles per Hour (mph)")
        print("2. Miles per Hour (mph) to Kilometers per Hour (km/h)")
        print("-----------------------------------------------------")
        category = get_int_input("Enter your choice (1/2): ")

        if category == 1:

            kilometers = get_float_input("Enter Speed in Kilometers per Hour (km/h): ")
            miles = kilometers_to_miles(kilometers)
            print(f"{kilometers} Kilometers per Hour (km/h) is equal to {miles:.2f} Miles per Hour (mph).")

        elif category == 2:

            miles = get_float_input("Enter Speed in Miles per Hour (mph): ")
            kilometers = miles_to_kilometers(miles)
            print(f"{miles} Miles per Hour (mph) is equal to {kilometers:.2f} Kilometers per Hour (km/h).")

        else: 
            print("Invalid choice. try again :( ")
                
    else:
       print("Invalid choice. Please select 1/5.")

if __name__ == "__main__":

    while True:
        main()
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if another_conversion != 'yes':
            break