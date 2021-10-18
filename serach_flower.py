# Write your code here
# HINT: create a dictionary from flowers.txt

dict_flowers = {}

with open('flowers.txt') as f:
    for line in f:
        dict_flowers[line.split(": ")[0]] =line.split(": ")[1]

# HINT: create a function to ask for user's first and last name
def user_name():
    name =  input("Enter your First [space] Last name only:").title()
    return name

# print the desired output
name = user_name()
first_letter = name[0]
seach_flower = dict_flowers[first_letter]
print("Unique flower name with the first letter: {}".format(seach_flower).title())
