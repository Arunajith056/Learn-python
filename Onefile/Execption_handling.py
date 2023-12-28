# The try block contains the code that might raise an exception.
# The except block catches specific exceptions. You can catch multiple exceptions or use a more general except Exception block.
# The else block is executed if no exception occurs.
# The finally block is always executed, regardless of whether an exception occurred.
try:
	a=int(input("enter the number"))
	b=int(input("enter the number"))#give zero
	result = (a / b)
except ZeroDivisionError:
	print("Anything will be divisble by zero is Zero")	

except TypeError as e:
	print(e)
	print("plz enter numbers only ")
except Exception:
	print("some error occurred ")
else:
	print(result)
finally:
	print("bye")


