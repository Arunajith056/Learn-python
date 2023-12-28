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
		print("im riding in the bike"+ self.model)
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
	def ride(self):# method overriding we have ride in method in parent class 
		super().ride()# access the parent class methods
		print("i'm riding in the Electric Bike")

class Flight(Bike, Auto):
	def cm_1(self):
		super().cm_1()
		print("multiple from flight")


# Abstract class:
# 16. Abstract Classes and Interfaces:
# Abstract Classes:
# Cannot be instantiated.Define abstract methods that must be implemented by derived classes.
# Interfaces:
# Not a direct concept in Python.Achieved through conventions and abstract classes.

from abc import ABC,abstractmethod
class Vechile_(ABC):
	@abstractmethod
	def __init__(self,model,price):
		self.__model = model
		self.price = price
	def start(self):
		print(f"Engine started ready to Ride ")
		
	def stop(self):
		return "plz stop the vechicle"
		
class Car_(Vechile_):
    def __init__(self, model, price):
        super().__init__(model, price)
    def cars(self):
    	print(f'im in the toyata {self.price}')
   

# Creating an instance of the Car_ class
user = Car_("md222", 34444)
user.start()
user.cars()
print(user.stop())
user1 =Car_("model",3683)
user1.start()

# --- naming conventions ---

#public- use anywhere in class 
#private - cannot be used for the outside class (__) --dunder variable 
#protected - can be accessed by inherited class(_)
# internal variable --- if __name__ = __main___

def hello():
	print("Hello everyone")
	if __name__ == '__main__':
		print("this file run directly ")
	print(__name__)
hello()




