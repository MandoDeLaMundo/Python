x = [ [5,2,3], [15,8,9] ] 
# x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    # {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
    # 'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x)

# students[0]['last_name'] = "Bryant"
# print(students)

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

# z[0]['y'] = 30
# print(z)

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

def iterateDictionary(some_list):
    print(some_list)
# def iterate_dictionary(list):
    # for i in range(0, len(list)):
        # output = ""
        # for key,val in list[i].items():
            # output += f"{key} - {val},"
        # print(output)

iterateDictionary(students)
# iterate_dictionary(students)

def iterateDictionary2(key_name, some_list):
    print([key_name], [some_list])
# def iterate_dictionary2(key_name,list):
#     for i in range(0, len(list)):
#         for key,val in list[i].items():
#             if key == key_name:
#                 print(val)


iterateDictionary2('first_name', students)
# iterate_dictionary2('first_name',students)
# iterate_dictionary2('last_name',students)

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

def printInfo(some_dict):
    print(some_dict)
# def print_info(dict):
#     for key,val in dict.items():
#         print("-----------")
#         print(f"{len(val)} {key.upper()}")
#         for i in range(0, len(val)):
#             print(val[i])

printInfo(z)
# print_info(dojo)
