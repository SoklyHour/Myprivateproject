program = True
while program == True:
    
    name = input("Enter your name: ")
    Weight_in_kg = float(input("User currency weight in kilogram: "))
    Height_in_m = float(input("User currency height in meter: "))
    BMI = Weight_in_kg/(Height_in_m ** 2 )

    if (BMI < 18.5):
        print(f"{name} is underweight by {BMI} BMI")
    elif (BMI >= 18.5 and BMI < 24.9):
        print(f"{name} is normal by {BMI} BMI")
    elif (BMI >= 25 and BMI < 29.9):
        print(f"{name} is overweight by {BMI} BMI")
    elif (BMI >= 30 and BMI < 34.9):
        print(f"{name} is obese by {BMI} BMI")
    elif (BMI >= 35):
        print(f"{name} is extremely obese by {BMI} BMI")

    use_again = input("Do you want to re-run the program or quit?: (Y/N)")

    if use_again == "N":
        program = False
        print("Thank you for using our BMI APP!")

