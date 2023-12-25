# Lists
list1 = ["chennai", "salem", "trichy", "madurai"]
list2 =[1,2,3,4,5,6,1]
list3 =["chennai",35,"salem",45]
print(list1)
# access the list with index 
print(list1[0])
print(list1[:2])# also use negative index 
# modify the list with index 
list1[1] ="cuddalore"
print(list1)
add_list ="coimbatore", "kanyakumari"
# append 
list1.append(add_list)
list2.append("thiruvanamalai")
print(list1)
print(list2)
# insert the list in index position 
list1.insert(2,"villupuram")
print(list1)
#remove the items in list by del keyword and pop() method # some methods return the some value 
del list1[1]   #also give the index 
print(list1)
deleted = list1.pop(2)
print(f'{list1} and {deleted} is deleted from your list ')
# use remove by the value using remove method 
num =2
list2.remove(num)
print(list2)
# sorting
# temporary sort 
list5=[1,4,5,6,4,3]
print(sorted(list5))
#permanent sort 
print(list5)
list5.sort()
print(list5)
# reverse the list 
list5.reverse()
print(list5)
# length of the list 
length = len(list5)
print(len(list5))
print(length)
# sorted the mixed of the datatypes in list 
list6=[1,2.5,"chennai","hello",3,7,True]
sorted_list = sorted(list6, key=str)# to avoid the typeerror give the key=str that convert the all the data types 
print(sorted_list)
salar =['praphas','prithvraj']
salar.extend("yash")# extends iterate the value store the each one in list 
print(salar)
# 2dimensional list 
# copy -shallow copy and deep copy 
cities=["chennai","cuddalore","villupuram","thiruvanamalai"]
tn = cities 
andhra=["hydrabhad","telugana","thirupati"]
karnataka=["banglore","mysore"]
india=[tn,andhra,karnataka]# 2dimensional
cities.remove("chennai")
print(cities)
print(tn)#that will delete also in tn because of pointing the reference of the cities memory location 
# create in new location use shallow copy for 1dimensional list 
tn = cities[:]
# now remove or modify something see the changes
cities.remove("villupuram")
print(cities)
print(tn)
#deep copy for 2dimensional list 
import copy 
india_state = copy.deepcopy(india)
print(india_state)
# function -count,index,
# use loop and conditional statements