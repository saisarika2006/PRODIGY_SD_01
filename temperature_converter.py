temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ").strip().lower()

if unit == "celsius":
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print(f"Fahrenheit: {fahrenheit:.2f}")
    print(f"Kelvin: {kelvin:.2f}")

elif unit == "fahrenheit":
    celsius = (temperature - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"Celsius: {celsius:.2f}")
    print(f"Kelvin: {kelvin:.2f}")

elif unit == "kelvin":
    celsius = temperature - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"Celsius: {celsius:.2f}")
    print(f"Fahrenheit: {fahrenheit:.2f}")

else:
    print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")
