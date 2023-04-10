# a = """lorem ipsun dolor is  """

# print(a)

# a = "hello, world!"
# print(len(a))

# txt ="the best things in life are free!"
# if "expensive" in txt:

# a = "Hello, World!"
# print(a.split(",")) 

# def sum_int_or_str(a, b):
#      return int(a) + int(b)

# assert(sum_int_or_str(1, '2')) == 3
# assert(sum_int_or_str(2, 2)) == 4


# def get_second_character(a):
#     "get second character, if only 1 character return 0"
#     if len(a) > 1:
#          return a[1]
#     else:
#          return 0


# assert(get_second_character("ab")) == "b"
# assert(get_second_character("a")) == 0

# car = {
#      'brand': 'Toyota',
#      'year': 2022
# }

# assert(car['brand']) == 'Toyota'


# cars =[ 
#      {
#      'brand': 'Toyota'
#      },
#      {
#      'brand': 'Honda'
#      }    
# ]

# assert(cars[1]['brand']) == 'Honda'

# cars =[
#      {
#         'brand': 'Toyota'
#      },
#      {
#         'brand': 'Honda',
#         'products': [
#             'civic'
#         ]
#      }
# ]

# assert(cars[1]['products'][0]) == 'civic'

# raw_cars = 'toyota,honda,indiacar'
# assert(raw_cars.split(',')) == [
#      'toyota', 'honda', 'indiacar'] # trun raw_cars into a list

# raw_cars = raw_cars.upper()

# assert(raw_cars.split(',')) == ['TOYOTA', 'HONDA', 'INDIACAR'] 

# # raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'
# # # 1 step split
# # # 2 step casting to set, return {''}
# # # 3 step casting back to list, {''}
# # raw_cars = raw_cars.split(',')
# # raw_cars = set(raw_cars)
# # raw_cars =list(raw_cars)
# # assert() == ['toyota','honda', 'indiacar']

# raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'
# raw_cars =raw_cars.split(',')
# raw_cars =set(raw_cars)
# raw_cars =len(raw_cars)
# assert(raw_cars) == 3

# a = "hello"
# b = "world"
# c = a + " " + b
# print(c)

# for x in "banana":
#      print(x)

# age = 36 
# txt = "My name is jhon, and I an .."
# print(txt.format(age))

# x = y = z = "0range"
# print(x)
# print(y)
# print(z)


# fruits = ["apple", "banana", "cherry"]
# x, y ,z =fruits
# print(x)
# print(y)
# print(z)


# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z) # ,


# x = 10
# y = 5
# print(x + y) 


# x = "awesome"

# def Myfunction():
#     print("python is "+ x)

# Myfunction()    


# def myfunction():
#     global x 
#     x = "fantastic"

# myfunction()

# print("pythom is " + x)


# import random
# print(random.randrange(1,10))

# list1 =["apple", "banana", "cherry"]
# list2 =[1, 5, 7, 9, 3]
# list3 =[True,False,False]

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1]) # -1,-2

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1,"orange") #append
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineple", "pepaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ["mango", "pineple",]
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1) # untuk menghapus menggunakan index
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0] 
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("apple") #untuk menghilangkan salah satu index
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear() # untuk menghapus 
# print(thislist)

# thistuple = ('banana', 'apple', 'cherry')
# print(thistuple)

# thisset = {'apple', 'banana','cherry'}
# print(thisset)

# thisset = {'apple', 'banana', 'cheryy'}
# thisset.add('orange')
# print(thisset)

# thisdict = {
#     "brand" : "ford",
#     "model" : "jdjd",
#     "year" : 1213
# }
# print(thisdict["brand"])