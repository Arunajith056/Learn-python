# objects - properties -key and value pair 
#retrevive the data using key 
dict_my = {
	"name":"ram",
	"age":24
}
print(dict_my)
print(dict_my["name"])
#Adding a new key value pair 
dict_my["city"]="chennai"
print(dict_my)
# modify the dict_myionary 
dict_my["city"]="coimbatore"
print(dict_my)
print(dict_my.items())# get key and value 
# delete the items
del dict_my["city"]
print(dict_my)
#looping key and value 
for key,value in dict_my.items():
	print(key,value)
for key in dict_my.keys(): # acess key 
	print(key)
dict_my = {
    "person1": {"name": "ram", "age": 24, "city": "chennai"},
    "person2": {"name": "shyam", "age": 30, "city": "coimbatore"}
}
job={"riya":"infosys","ramya":"tcs","megha":"amazon"}
for company in job.values():
	print(company)
# Accessing values using items["name"]
for key, items in dict_my.items():
    print(items["name"])
person1_data = dict_my["person1"]["name"]
print(f'person one data {person1_data}')
# in for loop
for key, items in dict_my.items():
	if key == "person2":
		print(items["name"])
# key must in unique that will be override the first name
my_dict ={"name":"Ajithkumar","name":"ram_3"}
print(my_dict["name"])
#use also 
#list in dictionaries
my_dict={"name":["Ajithkumar","ram"]}# define the values in list 
firstname = my_dict["name"][0]
print(firstname)
#list of dictionary 
my_listdict=[{"name":"ravi","age":25,"job":"developer"},{"name":"venget","age":25,"job":"electrican"}]
print(my_listdict[0]["job"])
my_listdict[0]["salary"] = "60000"
print(my_listdict[0])