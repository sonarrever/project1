#list1 = [1, 2, 3, "a"]
# a = list + [1<2]
#cash = [1235, 3751, 65423, 76543]
# rashod = 0.2
# schet = 0
# for i in cash:
#     schet = schet + i
#
# prybyl = schet - (schet * rashod)
# print (prybyl)


# def get_cash(cash_list< rashod):
#     schet = 0
#     for i in cash_list:
#         schet = schet + i
#     prybyl = schet (schet * rashod)
#     return prybyl
#
#
#    print (get_cash(cash< rashod))

# args, kwargs


# def get(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
#
# get(1, "a", True, a=10, b=False)


# def kpi(**kwargs):
#     count = len(kwargs)
# print(count)
#     schet = 0
#     for x in kwargs.values():
#         schet += x
#     return schet/count
#
# kpi( mat=100, fiz=90)
# print(kpi(mat=100, fiz=90))


# dict1 = {"k": 1, "h": 4, "bool": True}
# for x, y in dict1.items():
#     print(x, y)


def get_num(*args):
    a = 0
    for i in args:
        if type(i) == int:
            a+=i

    return a

print(get_num(1,  False, 32, 4, 5, "True", ["a", "v"])










