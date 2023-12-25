# functions are block of reusable code is designed perform a specific task 
# parameter and arguments
#variable scope- local variable and global variable
#variable length arguments (*args)-store in tuple 
    #keyword arguments - (**kwargs)- store in dictionary 
# passing list and dictionary of arguments 
# return the list and dictionary 
# ''' using for documention for functions is known as Docstring'''
greet_all ="Welcome"  #globle variable
def greet(name):#name variable for this function is parameter 
	'''Function get name from user and print the name'''
	print(name) 
greet("Robin hood")#passing the value (arguments)-positional arguments

# variable scope
def greet1(n):
	greet2_all="Hello everyone" #local variable only access in the function
	'''change the global variable in local using global keyword'''
	global greet_all 
	greet_all = "Changed_Welcome"
	print(n)
	print(greet2_all)
greet1(greet_all)# assign global variable to the arguments
#print(greet2_all) - try it gives the nameerror
print(greet_all)

# Default parameters
def greet_default(name, age=24): #give value by default is the default parameters
	''' ONLY give the arguments to the name , age is not required but u give also'''
	print(f'your name is {name} and your age is  { age }')
greet_default("Ajith") # passing one arguments error will not come 

# keyword arguments 
def greet_keyword(name, age):
	''' Assign the parameter fo value in arguments '''
	print(f'by keyword your name is {name} and your age is {age}')
greet_keyword(age=24, name="Ajith")

#return Something in the function as required 
def sum(a,b):
	return a+b 
print(sum(2,3))

''' variable length Arguments '''
# *args (Arbitrary Positional Arguments):
# Allows a function to accept a variable number of positional arguments.
def variable_n(*args):
	num = 0
	for i in args:
		num += i
	return num 
print(variable_n(1,2,3,4,5,))


#recursion function
#A function can call itself. This is known as recursion
def fact(num):
	''' num from user get factorial of num'''
	if num == 0:                  
		return 1
	return num*fact(num-1) 

print(fact(4))

#Generators
#Generators allow you to create iterators in a more concise way. They use the yield keyword to produce a series of values.
def sum_num(num):
	for i in range(0,num+1):
		print(i*i)
sum_num(5)
#but in generator
def sum_gen(num):
	for i in range(0,num+1):
		yield i*i
gen_output = sum_gen(5)
print(gen_output)
for i in gen_output:
	print(i)
