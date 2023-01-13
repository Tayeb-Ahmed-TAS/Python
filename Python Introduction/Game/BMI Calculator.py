# BMI Calculator
# ? Formula for kb/m, BMI = kg / m ^ 2
# ? Formula for lbs/inch, BMI = (703 * lbs) / inch ^ 2


def measurements():

    print("1. Kilograms and meters\n2. Pounds and inches")

    measurement = int(input("1 or 2 ? => "))

    if measurement == 1:

        kg_m()

    elif measurement == 2:

        lb_inch()

    else:

        print("Wrong Input ! Select again")

        measurements()


def kg_m():

    weight = float(input("Enter weight in kg => "))

    height = float(input("Enter height in meters => "))

    bmi = weight / pow(height, 2)

    BMI_ind(bmi)


def lb_inch():

    weight = float(input("Enter weight in lbs => "))

    height = float(input("Enter height in inch => "))

    bmi = (703 * weight) / pow(height, 2)

    BMI_ind(bmi)


def BMI_ind(bmi_val):

    bmi_list = ["Under Weight", "Normal Weight", "Over Weight", "Obesity"]

    bmi_rsl = "BMI retult : "

    if bmi_val < 18.5:

        print(f"{bmi_rsl} {bmi_list[0]} ({format(bmi_val,'.2f')})")

    elif bmi_val >= 18.5 and bmi_val < 25:

        print(f"{bmi_rsl} {bmi_list[1]} ({format(bmi_val,'.2f')})")

    elif bmi_val >= 25 and bmi_val < 30:

        print(f"{bmi_rsl} {bmi_list[2]} ({format(bmi_val,'.2f')})")

    elif bmi_val >= 30:

        print(f"{bmi_rsl} {bmi_list[3]} ({format(bmi_val,'.2f')})")


print("\t\tBMI Calculator\n\nSelect Measurement Units")

measurements()
