# import time
# import math

# def calculate_time(func):

#     def inner1(*args, **kwargs):

#         begin = time.time()

#         func(*args, **kwargs)


#         end = time.time()
#         print("Total time taken in : ", func.__name__, end - begin)

#     return inner1

# @calculate_time
# def factorial(num):

#     time.sleep(2)
#     print(math.factorial(num))

# factorial(10)

# import requests
# from pprint import pprint

# r = requests.get('https://jsonplaceholder.typicode.com/posts/101')
# data = r.json()
# pprint(data)

# post = {
#     'body': "Lorem ipsun",
#     'title':"Title",
#     'userId':5,
# }

# req = requests.post('https://jsonplaceholder.typicode.com/posts', json=post)
# print(req.json())
# print('Status_code: ', req.status_code)

# update_post = post
# update_post['id'] = 5

# req = requests.put(
#     'https://jsonplaceholder.typicode.com/posts/5', json=update_post)
# print(req.json())



# square = lambda x: x ** 2
# print(square(2))



# print("Menghitung Luas Segetiga ")
# print("=========================")
# a = int(input("Masukan alas: "))
# t = int(input("Masukan tinggi: "))
# luas = 0.5*a*t
# print("Luas segitiga dari alas", a ," tinggi",t ,"adalah: ", str(luas))