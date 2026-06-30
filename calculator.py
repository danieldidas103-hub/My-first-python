# python calculator
operator=input("enter operator (-  *  / + ): ")

num1=float(input("enter num1: "))

num2=float(input("enter the num2: "))

if operator=="+":
	result=(num1 + num2)
	print(result)
	
elif operator=="-":
	result=(num1 - num2)
	print(result)

elif operator=="*":
	result=(num1 * num2)
	print(result)

elif operator=="/":
	if num2==0:
		print("ERROR: no division of zero number")
		
	else:
		result=(num1 / num2)
		print(result)
	
else:
	print(f"the operator is invalid")
