user_name = 'pleasant'
x = user_name.capitalize()
print(x)
user_email = 'GOODWILL@GMAIL.COM'
y = user_email.casefold()
print(y)

Language = "Spanish"
for x in Language:
    print(x)
    if x == "n":
        break

store_list = [['Eggs', 'tomatoes', 'pepper'], ['milk', 'yogourt', 'butter'], ['doughnut', 'fries','chips']]
for item in store_list:
    print(item)
    for i in item:
        if i == 'doughnut':
            break
        print(i)

