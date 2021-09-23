#генераторы списка
# lists = []
# for i in range(0, 100):
#     lists.append(i)
#     print(lists)

# list2 = [x for x in range(100)]
# print(list2)

# lists = []
# for i in range(1, 1000):
#     if i % 3 == 0:
#         lists.append(i)
#
# print(lists)

# lists = [x for x in range(1, 100) if x % 3 ==0]
# print(lists)

# lists = []
# for i in range(-100, 50):
#     if i % 3 == 0 and i % 5 == 0:
#         #pow(i,3)
#         number = abs(i**3)
#         lists.append(number)
# print(lists)


# lists = [abs(pow(x, 3)) for x in range(-100,50) if x % 3 ==0 and x % 5 ==0]
# print(lists)

# def filter_list(range1, range2):
#     lists = [abs(pow(x, 3)) for x in range(range1, range2) if x % 3 == 0 and x % 5 == 0]
#     return lists

# list1 = filter_list(-100,100)
# print(list1)
#
# kyial = {
#     "home": "2этаж",
#     "car": "BMW X7"
# }
# saikal = {
#     "home": "4этаж",
#     "car": "toyota"
# }
#
# eldar = {
#     "home": "6этаж",
#     "car": "mers 222"
# }
# python_boot = [eldar, saikal, kyial]
# car = [x.get("car") for x in python_boot]
# for i in python_boot:
#     car.append(i.get("car"))
# print(car)

#
# from datetime import datetime
# def func1():
#     lists = []
#     start = datetime.now()
#     for i in range(1, 100700):
#         lists.append(i)
#     end = datetime.now() - start
#     print ("время для цикла for", end)
#     return lists
#
# def func2():
#     start = datetime.now()
#     lists = [x for x in range(1, 100700)]
#     end = datetime.now() - start
#     print("время list comprehention", end)
#     return lists
# func1()
# func2()

# from datetime import datetime
# def time(func):
#     def wrapper():
#         start = datetime.now()
#         func()
#         end = datetime.now() - start
#         print (end)
#     return wrapper
#
#
# @time
# def func1():
#     lists = []
#     for i in range(1, 10000):
#         lists.append(i)
#         return lists
#
# @time
# def func2():
#     lists = [x for x in range(1, 10000)]
# func1()
# func2()


# def humburger(cotlet):
#     def wrapper():
#         print("верхняя булочка")
#         print("майонез")
#         print("верхний салат")
#         cotleta()
#         print("нижний салат")
#         print("майонез")
#         print("нижняя булочка")
#
#     return wrapper
#
# @humburger
# def cotleta():
#     print("сочная котлета")
# cotleta()

#
# def humburger(cotlet):
#     def wrapper(*arg, **kwargs):
#         print("verh bulochka")
#         cotlet(*arg, **kwargs)
#         print("nij bulochka")
#
#
# @humburger
# def cotlet(ingridient):
#     print("cotlet iz{}".format() ingridient"))
#     cotlet("chicken")


# lists = ["kyial","saikal","meerim", "iskender"]
# print(f"m-{lists[1]}-{lists[2]}")
# print("{0}{2}{3}".format(lists[1],lists[3],lists[0],lists[2]))


#
# d = {
#     "name": "Vika",
#     "age":18,
#     }
# a = d.pop("name")
# d.update({"name":"Eldar"})
# print(len(d))

#print(d)
#print(name)
#dict()

#import math
# pow()
# len()
# abs()
# round()
# math.sqrt()
# sum()
# maxmin()
# print(pow(3, 2))
# print(math.sqrt(4))


# number = int(input("enter number: "))
# def fact(num):
#     count = 1
#     for i in range(1, num+1):
#         count *= i
#     return count
#
# print(fact(number))











