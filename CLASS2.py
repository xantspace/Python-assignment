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
