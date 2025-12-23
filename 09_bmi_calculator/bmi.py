"""BMI Calculator"""
def calc_bmi(w, h):
      bmi = w / (h ** 2)
      if bmi < 18.5: return bmi, "Underweight"
elif bmi < 25: return bmi, "Normal"
elif bmi < 30: return bmi, "Overweight"
    return bmi, "Obese"

w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
b, c = calc_bmi(w, h)
print(f"BMI: {b:.1f} - {c}")
