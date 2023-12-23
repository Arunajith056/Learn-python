# loop - repeats the set of code until the condition 
# check the alpthapet or not 
# letter = ""
# while not letter.isalpha(): 
# 	letter = str(input("enter the alphapet: "))
# print(f'{letter} is alphapet')
# # print the number to 100 by iteration
# num =1
# while num <=100:
# 	print(num)
# 	num += 1 # num = num+1
# print("bye")
# # for loop using range and append in list 
# list=[]
# for i in range(1,100+1):
# 	list.append(i)
# print(list)
# result = []
# # iterate the list 
# list = [1,2,4,"str","float"]
# for i in list:
# 	print(i)
# #guess the number game 
# import random
# num = random.randint(1,10)

# attempt=1
# while attempt <4 :
# 	guess = int(input("enter the guessing number: "))
# 	if guess > num:
# 		print(f'you entered number {guess} is greater then guessing number')
# 	elif guess < num:
# 		print(f'you entered number {guess} is lesser then guessing number')
# 	elif guess == num: 
# 		print(f'you won')
# 		break
# 	attempt += 1
# else:
# 	print(f'you lost ')
# list =[1,-3,3,5,6-7,6]
# positive_numbers = [num for num in list if num >=0]
# negative_numbers = [num for num in list if num <0 ]
# result = positive_numbers+negative_numbers
# print(result)
# get num from user store in list
# list_num = []

# while True:
#     inp = input("Enter the number: ")

#     if inp.lower() == 'stop':
#         break

#     try:
#         num = float(inp)
#         list_num.append(num)
#     except ValueError:
#         print("Invalid input. Please enter a number or type 'stop' to end the input.")

# print("List of numbers:", list_num)


# # nested loop
# for i in range(1,6):# no of row
# 	for j in range(1,6):# no of columns 
# 		print(i, end='') # end print in the same line 
# 	print("")
#remove the , string 
# str1= "A,D,D,F,G,S,A"
# str2= ''
# for i in str1:
# 	if i != ",":
# 		str2= str2+i
# print(str2)
#pass and continue also use in if else 
# Example 1: Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Example 2: Iterate over elements in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 3: Use enumerate to get both index and value
for index, value in enumerate(fruits):
    print(index, value)
num =[1,2,3,4,4,3,]
for index,value in enumerate(num):
	print(index, value)