"""
#interpretor little slow compare to compiler 
#  variables 
name = "Ajithkumar" #name -variable
print(name)
print("Hi"+ name)#concatination
age = 24
print (age)
Last = "kaka"
print(Last)
# use quotes for avoid afasrophe
book ="ram's story"
# method and function almost same
# funcion is directly call
# invoke the variable
print(book.title())
# \n and \t escape
print("ajith \n kumar")
# string methods ex- len,find,count,replace,isaplha,isdigit
print(len(book))
print(book.find("b"))
print(book.count("a"))
print(book.islower())
# multiple Assigments
name, age,details="ajith",24,"have a nice day"
like=dislike=comment= 100
print(details)
print(str(like)+str(dislike))
#type casting is concatenate with other datatype
otp=4984949#change integer to string 
print("your is otp"+ str(otp))
#Data type -str,int,float,boolean
b="10.5"
c=20
print(round(float(b)) + 2)
#Assignment
name ="Anand"
n=15
year=2021
print("Dear "+name+"\nyou have "+str(n)+" days leave"+"\nyear("+str(year)+")")
#formatted string literal
message = f'dear {name} \nyou have {n} days leave \nyear({year})'
print(message)
#user input 
name = input("what is your name")
age = input("enter your age:")
print(f'Hello {name} and your age is {age}')
Heigth = float(input("enter your Heigth:"))
Heigth_inches = f"{Heigth/2.45:.2f}"
print(Heigth_inches)
Emailid = input("enter your email: ")
phone_number  = input("enter your number ")
print(f'UserName:{name}\nEmail:{Emailid}\nPh:{phone_number}')
# math operation"""
# string slicing
# index position
# slicing[start:stop:step]
# name ="Ajithkumar"
# print(name[0:5])
# print(name[5:])
# print(name[::-1])
# print(name[-5:-1])
# print(name[2:-5])
# # slicing method 
# x= slice(2,8)
# y= slice(0,5)
# z=slice(2,8,2)
# print(name[x])
# print(name[y])
# print(name[z])
# assigment -string method
# name = "Happy"
# print(name[0])
# print(name[:2])
# print(name[:3])
# print(name[:4])
# print(name[:5])
# #reverse
# print(name[-1])
# print(name[-2:])
# print(name[-3:])
# print(name[-4:])
# print(name[-5:])


