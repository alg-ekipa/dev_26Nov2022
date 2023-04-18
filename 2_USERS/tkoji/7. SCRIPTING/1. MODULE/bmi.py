
# BMI = ()

def gather_info():
    height = float(input('What is your height? '))
    weight = float(input('What is your weight? '))
    system = input("Matric or Imperial units? ").lower().strip()
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Retrun the Body Mass Index over the given
    wheight, height, and measurment system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2) )
    else:
        bmi = 703 * (weight / (height **2 ))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight=weight, height=height, system=system)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Incorrect input.")
