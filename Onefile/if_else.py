# control flow 
# if, else, elif (conditional statements)
# relational operators 
a= 100
b=20
# comparison operator and logical operators
c=True
if c:
	if a >= 500:
		print("Hi")
else:
	print("is false value")
if a != b:
	print("yes not equal")
else:
	print("no is equal")



# age check ---
# num = int(input("enter your age: "))
# if num >=18 :
# 	print("your are eligible for vote")
# else:
# 	print("your not eligible for vote")
# 	number comparison -----
# num1 = int(input("enter the number1: "))
# num2 = int(input("enter the number2: "))
# if num1 < num2:
# 	print(f'{num1} is lesser than {num2}')
# elif num1 > num2:
# 	print(f'{num1} is greater than {num2}')
# else:
# 	print("both are equal")
# 	check even or odd number ---------
# num = int(input("enter the number: "))
# if num%2 != 0:
# 	print(f'{num} is odd number ')
# else:
# 	print(f'{num} is even number')
# 	leap year ----
# num= int(input("enter your number: "))
# if num%4 != 0:
# 	print(f'{num} is not leap year ')
# else:
# 	if num%100 != 0:
# 		print(f'{num } is a leap year ')
# 	else:
# 		if num%400 != 0: 
# 			print(f'{num } is not leap year ')
# 		else:
# 			print(f'{num }is a leap year ')
#simple calculator ----------
# operator = input("enter any operator: +, -, %, /, *: ")
# num1 = int(input("enter the number1: "))
# num2 = int(input("enter the number2: "))
# if operator == "+":
# 	print(num1+num2)
# elif operator == "-":
# 	print(num1-num2)
# elif operator == "/":    # try zero division error in error handling 
# 	if num2 !=0:
# 		print(int(num1/num2))
# 	else:
# 		print("zero divisble any number is zero try another number")
# elif operator == "*":
# 	print(num1*num2)
# else:
# 	print("wrong operator select correct one ")
# 	-----find  the largesrt number 
# num1 = int(input("first number: "))
# num2 = int(input("second number: "))
# num3 = int(input("third number: "))
# if num1 > num2 and num1 > num3:
# 	print(f'{num1} is largest number ')
# elif num2>num1 and num2>num3:
# 	print(f'{num2} is the largest number ')
# else:
# 	print(f'{num3} is the largest number')
# Always order the condition in  higher to lower for correct condition
# ternary operators or conditional expressions
user_text = str(input("enter something"))
print("hello") if user_text.lower()== "hello" else print("oops") #first tell the condition for if and else part 
# can also use the elif condition
# give the if after the else that consider as elif condition  
print("hello") if user_text.lower()=="hello" else print("bye") if user_text.lower()=="bye"else print("oops")


