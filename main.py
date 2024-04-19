my_string = "LaunchCode"

# a) Use string methods to remove the first three characters from the string and add them to the end.

print(my_string[3:]+my_string[:3])

# Use a template literal to print the original and modified string in a descriptive phrase.

print(f"The original string is {my_string} and the modified string is {my_string[3:]+my_string[:3]}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

user_input = input("Enter the number of letters that will be relocated: ")

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
if int(user_input) > len(my_string):
  print(f"Error: {user_input} is greater than the length of the string.")

else:
  print(f"The original string is {my_string} and the modified string is {my_string[int(user_input):]+my_string[:int(user_input)]}")

proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

for string in strings:
  if ',' in string:
    print(f"{string} is separated by commas.")
  elif ';' in string:
    print(f"{string} is separated by semicolons.")
  elif ' ' in string:
    print(f"{string} is separated by spaces.")  
  else:
    print(f"{string} is not separated by commas, semicolons, or spaces.")

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

for string in strings:
  if ',' in string:
    print(f"{string} is separated by commas.")
    print(f"The original list is {string}.")
    print(f"The new list is {','.join(string.split(',')[::-1])}.")
    
# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
for string in strings:
  if ';' in string:
    print(f"{string} is separated by semicolons.")
    print(f"The original list is {string}.")
    print(f"The new list is {','.join(sorted(string.split(';')))}.")
    
# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

for string in strings:
  if ' ' in string:
    print(f"{string} is separated by spaces.")
    print(f"The original list is {string}.")
    print(f"The new list is {','.join(sorted(string.split(' '), reverse=True))}.")

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
for string in strings:
  if ', ' in string:
    print(f"{string} is separated by comma spaces.")
    print(f"The original list is {string}.")
    print(f"The new list is {','.join(string.split(', ')[::-1])}.")

food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.

food_cabinet = food.split(',')
food_cabinet.sort()
print(food_cabinet)

equipment_cabinet = equipment.split(',')
equipment_cabinet.sort()
print(equipment_cabinet)

pets_cabinet = pets.split(',')
pets_cabinet.sort()
print(pets_cabinet)

sleep_aids_cabinet = sleep_aids.split(',')
sleep_aids_cabinet.sort()
print(sleep_aids_cabinet)

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_cabinet, equipment_cabinet, pets_cabinet, sleep_aids_cabinet]
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

user_input = input("Select a cabinet (0-3): ")

# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.

if int(user_input) < 0 or int(user_input) > 3:
  print("Error: Invalid cabinet number.")
else:
  print(f"The contents of cabinet {user_input} are {cargo_hold[int(user_input)]}.")
  
# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

user_input_cabinet = input("Select a cabinet (0-3): ")
user_input_item = input("Select an item: ")
if int(user_input_cabinet) < 0 or int(user_input_cabinet) > 3:
  print("Error: Invalid cabinet number.")
elif user_input_item in cargo_hold[int(user_input_cabinet)]:
  print(f"Cabinet {user_input_cabinet} DOES contain {user_input_item}.")
else:
  print(f"Cabinet {user_input_cabinet} DOES NOT contain {user_input_item}.")