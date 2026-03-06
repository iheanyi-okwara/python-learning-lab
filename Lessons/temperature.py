# Temperature Converter in Python
# This program converts temperatures between Celsius and Fahrenheit.

'''
# Display a menu to the user.
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Ask the user for their choice.
choice = input("Enter choice (1 or 2): ")

# Ask the user for the temperature to convert.
temp = float(input("Enter temperature: "))

# Perform the conversion based on the user's choice.
if choice == '1':
    # Convert Celsius to Fahrenheit.
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {fahrenheit}°F")
elif choice == '2':
    # Convert Fahrenheit to Celsius.
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")

'''

# Loop Version of the Temperature Converter:
# This version allows the user to perform multiple conversions without restarting the program.
while True:
    # Display a menu to the user.
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    # Ask the user for their choice.
    choice = input("Enter choice (1, 2, or 3): ")

    if choice == '3':
        print("Exiting the temperature converter. Goodbye!")
        break

    # Ask the user for the temperature to convert.
    temp = float(input("Enter temperature: "))

    # Perform the conversion based on the user's choice.
    if choice == '1':
        # Convert Celsius to Fahrenheit.
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {fahrenheit}°F")
    elif choice == '2':
        # Convert Fahrenheit to Celsius.
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {celsius}°C")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
