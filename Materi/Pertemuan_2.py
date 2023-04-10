# thislist = ["aplle", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist


# thislist = ["apple","banana", "cherry", "orange", "kiwi","mango"]
# thislist[1:3] = ["blackcurrant","watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2,"watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ['apple' , 'banana']

# thislist = ["apple", "banana"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana","mango"]
# [print(x) for x in thislist]

# thislist = ["apple", "banana","mango"]
# thislist.pop(1)
# assert(thislist) == ["apple", "mango"]

# thislist.append("kiwi")
# assert(thislist) == [ "apple", "mango", "kiwi"]


# new_list = ["apple", "apple", "apple","apple", 
#             "mango", "kiwi","apple","apple",
#             "apple", "apple"]
# assert(new_list[4:6]) == ["mango","kiwi"]



# new_list = ["apple", "apple", "apple","apple", 
#             "mango", "kiwi","apple","apple",
#             "mango","kiwi",
#             "apple", "apple"]

#  assert([x if for in new_list if x != "apple"]) == ["mango", "kiwi","mango", "kiwi"]

# list  = [ 1, 4 , 5, 6, 2, 4]

# assert([x for x in list if x != 4]) == [1, 5, 6, 2]

# list1 [1, 4, 5, 7]

# list3 = list1.copy()
# list3.pop()

# assert(list3) == [1, 4, 5]
# assert(list1) == list1


# fruits = ("apple", "banana", "cherry", "strauberry", "raspberry")

# (green,yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# cars = {
#     'brand' : 'honda',
#     'product':'civic'
# }

# print(cars['brand'])

# print(cars.keys())

# for key in cars.keys():
#     print(cars[key])



# cars = {
#     'brand': 'honda',
#     'product': 'civic'
# }
# print(cars.values())

# print(cars.get('year',None))
# print('Tidak akan dijalankan')

# if 'year'in cars:
#     print(cars['year']) #cars.get ('year', None)


# cars.update(
#     {
    
#     'year' : 2020,
#     'key' : 2121

#     }
    
# )

# cars['year'] = 2020
# print(cars)

# cars['brand'] = 'Toyota'
# print(cars)


# def my_function(fname):
#     print(fname+ "Rafsnes")

# my_function("Email")
# my_function("Tobias")
# my_function("Linus")


# def my_function(*kids):
#     print(kids)
#     for kid in kids:
#         print(kid)

# my_function("Email", "Tobias")   


# def my_function_2(child1, child2):
#     print(child2)

# my_function_2(child2="Email", child1="Tobias")


# def full_name(first_name, last_name):
#     print(first_name + " " + last_name)

# full_name(last_name="Tobias", first_name="Emil")



# def detail_people(**data):
#     print(data)

# detail_people(
#     nama_depan="saha",
#     nama_belakang="itu",
#     umur="20",
#     status="bekerja"
# )

# detail_people(
#     nama_depan="saha",
#     nama_belakang="itu",
#     umur="20",
  
# )

# def multiply_by_two(free):
#     return 2 * free

# assert(multiply_by_two(3)) == 6


# def multiply_by_x(w, x = 2):
#     "if x not passed, then define teh default value to 2"
#     return w * x 

# assert(multiply_by_x(3)) == 6
# assert(multiply_by_x(3, 1)) == 3

# user_input = input('iput dikali dengan 2: ')
# print(multiply_by_two(int(user_input)))

# how_many_input = input("berapa kali ingin input data? ")
# i = 0 
# while i < int (how_many_input):
#     user_input = input ('input dikali dengan 2: ')
#     print(multiply_by_two(int(user_input)))
#     i += 1

# how_many_input = input("berapa kali ingin input data? ")
# i = 0 
# while True:

#     if i == 0:
#         break

#     user_input = input ('input dikali dengan 2: ')
#     print(multiply_by_two(int(user_input)))
#     i += 1

# def avg(grades):
#     grade = 0 
#     grades = grades.split(',')
#     for i in grades:
#         grade += float(i)
#     grade = grade/len(grades)
#     return grade

# how_many_input =input("Enter then number of students in your class: ")

# students = []

# for i in range(int(how_many_input)):
#     nama = input("Enter the name " + str(i+1) + ": ")
#     grades = input("Enter the grades " + str(i+1) + "(comma-separated): ")
#     students.append(
    
#     {
#         'nama' : nama,
#         'grade' : grades, 
#         'avg' : avg(grades)
#     }
#   )  
    
# print()
# print("averange grades: ")
# for x in students:
#     print(x["nama"], ":",  x["avg"])
