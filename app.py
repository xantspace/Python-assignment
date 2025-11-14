# This is FIRST ASSIGNMENT
print("My First assignment")
# This is SECTION A
word1 = 'Hello, '
word2 = "welcome "
word3 = """to python class"""
print(f"{word1}{word2}{word3}")

sentence = "Python is fun to learn"
print(sentence[4:9])

message = """
 Python is powerful.
 It is easy to learn.
 It is loved by developers
"""
print(message)

# This is SECTION B
text = "PYTHON"
print(text[0])
print(text[2])
print(text[5])

print("###")

language = "PYTHON"
for language in language:
    print(language)

print("###")
# This is SECTION C
fruit = "BANANA"
print(len(fruit))

word = "Learning Python is cool"
if "Python" in word:
    print("Yes! 'Python' is found.")
if "Java" in word:
    print("Yes! 'Java' is found.")
else:
    print("No! Java is not Available")

# BONUS ASSIGNMENT
msg = "Coding is fun"
count = 0
for n in msg:
    if n == "n":
        count += 1
print(count)

poem = """
Roses are red,
Violets are blue,
Python is rare,
And that's why it is cool.

"""
print(poem.upper())

# ## This is the second assignment
print("This the second assignment")
# #Section A Variables

name = "Ada"
age = 18
school = "Bright Future Academy"
print(f"My name is {name} and I am {age} years old. and i attend {school}")

country = "Nigeria"
capital = "Abuja"
print(f"The capital of {country} is {capital}")

first_name = "John"
middle_name = "Paul"
last_name = "Okoro"
print(f"{first_name} {middle_name} {last_name}")

food = "Rice"
drink = "Juice"
print(f"I love eating {food} and {drink}")

name = "Hello world"
print(name[6:])
print(name.replace("Hello", "Hey there!"))
print(name.split(","))

price = 30
print(f"i need ${price * 2} for my business")

msgs = "we are the so-called \"Vikings\" from the north"
print(msgs)

##Classwork 11/11/2025
print("This is the classwork for 11/11/2025")

work_txt = "It\'s alright"
print(work_txt)
work_txt1 = "This is python.. true\\false ."
print(work_txt1)
work_txt2 = "Rice\nBeans"
print(work_txt2)
work_txt3 = "Dear\rRonaldo"
print(work_txt3)
work_txt4 = "This\tAssignment"
print(work_txt4)
work_txt5 = "Dolapo \bFashion \bWorld!"
print(work_txt5)
work_txt6 = "\160\146\154\164\157" #backslash followed by three integers will give in an octal value:
print(work_txt6)
work_txt7 = "\x48\x65\x6c\x6c\x6f"
print(work_txt7)