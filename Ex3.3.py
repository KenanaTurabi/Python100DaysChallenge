BMI=round(weight/height**2)
if BMI < 18.5:
  print(f"your bmi is {BMI}, and you are underweight.")
elif BMI <25:
  print(f"your bmi is {BMI}, and you have a normal weight.")
elif BMI <30:
  print(f"your bmi is {BMI}, and you are slightly overweight.")
elif BMI <35:
  print(f"your bmi is {BMI}, and you are obese.")
else :
  print(f"your bmi is {BMI}, and you are clinically obese.")