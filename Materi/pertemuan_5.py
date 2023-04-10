# import datetime

# x = datetime.datetime.now()
# print(x)
# print(type(x))



# import datetime

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime('%D'))
# print(x.strftime('%m'))
# print(x.strftime('%Y'))




# import datetime

# x = datetime.datetime(2020, 5, 17)
# print(x)



# import datetime

# x = datetime.datetime.now()

# print(x)

# print(x.strftime('%d-%m-%Y'))

# arr_1 = [5, 78, 2, 0]

# assert(min(arr_1)) == 0
# assert(max(arr_1)) == 78

# #function 5 pangkat 5
# assert(pow(5, 5)) == 3125

# try:
#     f = open("demofile.txt")
#     try:
#         f.write("Lorem Ipsun")
#     except:
#         print("Something went wrong wrting ti the file")
#     finally:
#         f.close()
# except:
#     print("Something went wring openig the file")



# try:
#     print(x)
# except:
#     print("Semething went  wrong")
# finally:
#     print("The 'try except is finished")

# import json
# # some JSON:
# x = '{ "name":"John", "age":"30", "city":"New York"}'
# # parsen x:
# y = json.loads(x)
# #the result is a Python dictionary:
# print(y["age"])

# import json

# x = {
#     "name":"jhon",
#     "age":30,
#     "city":"Hew York"
# }

# y = json.dumps(x)

# print(y)


# f = open("demofile.txt" , "r")
# print(f.read())



# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close

# #open adn read the file after  teh appeding:
# f = open("demofile2.txt", "r")
# print(f.read())


# f = open("myfile.txt", "w")


# import json
# # 1. Opem file & read
# f = open('json_read.txt')

# json_string  =  f.read()
# print(json_string)

# # 2. Loads
# json_dict = json.loads(json_string)
# print(json_dict)
# print(type(json_dict))
# print()
