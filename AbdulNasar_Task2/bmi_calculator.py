
print("         BMI CALCULATOR")
print("-------------------------------------")

while True:
    try:
        weight = float(input("Enter your weight in kg: "))

        if weight <= 0:
            print("Please enter a positive weight")
            continue

        break

    except ValueError:
        print("Please enter a valid number for weight.")

while True:
    try:
        height = float(input("Enter your height in meters: "))

        if height <= 0:
            print("Please enter a positive height ")
            continue

        break

    except ValueError:
        print("Please enter a valid number for height.")

bmi = weight / (height * height)

print("\n------------------------------------")
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")
print("------------------------------------")

print("\nThank you for using the BMI Calculator!")