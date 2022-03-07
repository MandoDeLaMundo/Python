num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initualize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize list
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize lists
print(type(fruit)) # log statement
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') # add value
print(person['name']) # log statement
person['name'] = 'George' # variable declaration, change value
person['eye_color'] = 'blue' # variable declaration, change value
print(fruit[2]) # log statement

if num1 > 45: # if conditional, type check
    print("It's greater") # log statement
else: # else conditional
    print("It's lower") # log statement

if len(string) < 5: # if conditional, type check
    print("It's a short word!") # log statement
elif len(string) > 15: # else if conditional, type check
    print("It's a long word!") # log statement
else: # else conditional
    print("Just right!") # log statement

for x in range(5): # for loop, type check
    print(x) # log statement
for x in range(2,5): # for loop, type check
    print(x) # log statement
for x in range(2,10,3): # for loop, type check
    print(x) # log statement
x = 0 # variable declaration, initialize number
while(x < 5): # while loop
    print(x) # log statement
    x += 1 # add value

pizza_toppings.pop() # delete value
pizza_toppings.pop(1) # delete value

print(person) # log statement
person.pop('eye_color') # delete value
print(person) # log statement

for topping in pizza_toppings: # for loop, type check
    if topping == 'Pepperoni': # if conditional, type check
        continue #continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if conditional, type check
        break # break

def print_hello_ten_times(): # function parameter
    for num in range(10): # for loop, type check
        print('Hello') # log statement

print_hello_ten_times() # log statement

def print_hello_x_times(x):  # function parameter, log statement
    for num in range(x): # for loop, type check
        print('Hello') # log statement

print_hello_x_times(4) # log statement

def print_hello_x_or_ten_times(x = 10): # function parameter, log statement
    for num in range(x): # for loop, type check
        print('Hello') # log statement

print_hello_x_or_ten_times() # log statement
print_hello_x_or_ten_times(4) # log statement


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)