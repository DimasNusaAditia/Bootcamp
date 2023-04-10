# import datetime


# class Person:
#     def __init__(self, name, age):
#      self.name = name
#      self.age = age

#     def say_my_name(self):
#        print("Helo my name is " + self.name)

# person_1 =  Person("jhon", 32)
# person_1.name = "emil"
# print(person_1.say_my_name())


# class Mathematic:
#    def __init__(self):
#       self.value = 0

#    def incremenet(self):
#       self.value += 2
    
#    def decrement(self):
#       self.value -=2
   
#    def add(self, a, b):
#       return a + b
   
#    def substraction(self, a ,b):
#       return a - b
   
#    def multiply(self, a, b):
#       return a * b   

# math = Mathematic()

# print(math.add(1, 2))
# print(datetime.datetime.now())

class car:
    def __init__(self, brand, year ):
        self.brand = brand
        self.year = year
        self.door = "Closed"
        self.car = "off"

    def open(self):
        if self.door == "Closed":
            print('Door Has Oppend')
            self.door = 'Oppend'
        else:
            print('Door is closed')

    def close(self):
        if self.door == "Closed":
            print('Doon Has Oppend')
            self.door = 'Closed'
        else:
            print('Door Is Open')

    def on(self):
        if self.car == "OFF":
            print('Machine Has On')
            self.car = 'On'
        else:
            print('Machine Is On')

    def off(self):
        if self.car == "ON":
            print('Machine Has Off')
            self.car = 'Off'
        else:
            print('Machine Has On')

car_1 = car('Lamborghini', 2023)
car_1.open()
car_1.close()
car_1.on()
car_1.off()