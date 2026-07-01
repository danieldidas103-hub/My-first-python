#python body mass index BMI calculator

weight=float(input("enter you are weight in kg: "))

height=float(input("enter you are height in meters: "))

BMI=weight / (height**2)

if BMI <=18.5:
	print("the patient is underweight")

elif BMI<=25:
	print("the patient is normal heathly ")

elif BMI<=30:
	print("the patient is overweight")
	
else:
	print("the patient is obese")
