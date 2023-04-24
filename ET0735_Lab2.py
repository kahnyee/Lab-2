print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def calculate_bmi(height, weight):
    # Calculates BMI based on height and weight inputs.

    bmi = weight / (height ** 2)
    return bmi


def check_bmi_range(bmi):
    # Checks if BMI is within the healthy range (18.5 - 24.9).

    if bmi >= 18.5 and bmi <= 24.9:
        return "healthy"
    else:
        return "not healthy"


# Main program
num_people = int(input("How many people would you like to check? "))
for i in range(num_people):
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))

    bmi = calculate_bmi(height, weight)
    bmi_range = check_bmi_range(bmi)

    print(f"The BMI is {bmi:.2f}. This is {bmi_range}.")