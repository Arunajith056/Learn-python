# tuples-immutable cannot be changed use paranthess for syntax 
tup=(1,2,3,3)
print(tup)
#tup[1]=4- try to change the value using index that give typeerror because of tuble cannot be changed is immutable
# but reassign the variable
tup=(3,4,7)
print(tup)
# function -count,index,
# use loop and conditional statements
# also use 2dimensional tuple
for i in tup:
	print(i)
if tup:#if any value in tuple is true 
	print(True)
if 3 in tup:
	print("yes")
if 5 not in tup:
	print("also yes")