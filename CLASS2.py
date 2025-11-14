motors = ["Lexus", "Toyota", "Camry", "Benz"]
motors[0] = 'Glk'
motors[2] = 'Lexus'
motors.append('BMW')
motors.sort(reverse=True)

motors = []



fruits = ["apple", "banana", "cherry", "orange"]
#fruits.pop(2)
#fruits.remove("apple")
#print(fruits)

for fruits in range (len(fruits)):
    print(fruits)
#converting a tuple to a list and changing the content of the list
x = ("apple", "banana", "cherry", "orange")
y = list(x)
y[1] = "Kiwi"
x = tuple(y)
print(x)

#addind items to a list using the append method
thistuple = ("apple", "banana", "cherry", "orange")
z = list(thistuple)
z.extend(["mango", "papaya", "pineapple"])
thistuple = tuple(z)
print(thistuple)

objects = ("paw-paw", "cucumber", "cashew")
print(objects)
even_numbers = (2,4,6,8,10)
print(even_numbers)
multi_dat_li = ("str", 10, 0.1, ["Toyota", "Honda"], False, {"key":"value"})
print(multi_dat_li)
print(type(multi_dat_li))
print(multi_dat_li[0])
print(multi_dat_li[3])


fruits = ["apple", "banana", "cherry", "orange"]
fruits[3] = "Mango"
fruits = tuple(fruits)
print(fruits)

person = ("Pleasant", 13, "bende")
name, age, place = person
print(f"My name is {name} and i am {age} years old and i am from {place}.")

#Create a tuple of your 5 favourite foods
#print the first, middle, and last items
#convert it to a list and change one food
#convert it back to a tuple

foods = ("Spagetti", "Jollof-Rice", "Yam Porridge", "Egg Sauce")
print(foods[0])
print(foods[1])
print(foods[3])
z = list(foods)
z[2] = "Fried Rice"
z = tuple(z)
print(z)

#back to lessons
#DICTIONARIES
#it follows a principle
#keys are unique whilst values can be changed
student = {
    "name" : "Pleasant",
    "age"  : 13,
    "Location" : "Bende",
    "class" : "100L"

}
#accessing values in dictionaries
print(student["name"])
print(student.get("name"))

#changing values in a dictionary
student["age"] = 100
print(student["age"])

#to add keys and values to an already existing dictionary
student["School"] = "UNICAL"
print(student)

