class User:
	#class variable
	user = 0

	def __init__(self, username, age):# constructor
		self.username = username # instance variable 
		#variable store the value from instance of objects 
		self.age = age
		# access the class variable with class name
		User.user += 1
	def register(self):
		print(f'Registering by ----{self.username}')


# inheritance (parent(base,super class),child(derived, sub class))
# multiple and multilevel

class Vechile: 
	def __init__(self,model,price):
		self.model = model
		self.price = price
	def throttle(self):
		print("give the speed")
	def ride(self):
		print ("i am riding")
	# def cm_1(self):
	# 	print("multiple from vechile")
class Bike(Vechile):
	def twowheeler(self):
		print("im riding in the bike")
		print ("This is bike")
	# def cm_1(self):
	# 	print("multiple from bike")
class Bus():
	def bus(self):
		print("i'm from bus")
	def cm_1(self):
		print("multiple from bus")
class Auto(Bus):
	def auto(self):
		print (" im riding in the auto")
	# def cm_1(self):
	# 	print("multiple from auto")
class Evbike(Bike):
	def ride(self):# method overriding 
		super().ride()# access the parent class methods
		print("i'm riding in the Electric Bike")

class Flight(Bike, Auto):
	def cm_1(self):
		super().cm_1()
		print("multiple from fligth")


user = Flight("cm23", 100000)
user.cm_1()
user=Auto()
user.bus()
