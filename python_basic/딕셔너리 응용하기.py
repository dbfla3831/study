# dic1 = dict(name = "cat", age = 3)
# print(dic1)

# dic2 = dict(zip(["name", "age"],["cat", 3]))
# print(dic2)

# dic3 = dict([("name", "cat"), ("age", 3)])
# print(dic3)

# dic4 = dict({"name" : "cat", "age" : 3})
# print(dic4)

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# dic.setdefault('e')
# print(dic)

# dic.setdefault('f', 100)
# print(dic)

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# dic.update(a = 90)
# dic.update(e = 50)
# print(dic)

# dic.update(a = 100, f = 900)
# print(dic)

# dic = {1 : 'one', 2 : 'twe'}
# dic.update({1 : "ONE", 3 : "THREE"})
# # print(dic)

# dic.update([[2, "TWE"], [4 , "FOUR"]])
# print(dic)

# dic.update(zip([1, 2], ['one', 'twe']))
# print(dic)

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# dic.pop('a')
# print(dic)

# del dic['a']
# print(dic)

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# print(dic.popitem())
# print(dic)

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# dic.clear()
# print(dic)

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# print(dic.get('a'))

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# print(dic.items())

# print(dic.keys())

# print(dic.values())

# keys = ['a', 'b', 'c', 'd']
# dic = dict.fromkeys(keys)
# print(dic)

# dic2 = dict.fromkeys(keys, 100)
# print(dic2)

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# for i in dic:
#     print(i, end = ' ')

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# for i in dic.items():
#     print(i, end = ' ')

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# for key, val in dic.items():
#     print(key, val)

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# for key in dic.keys():
#     print(key, end = ' ')

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# for val in dic.values():
#     print(val, end = ' ')

# keys = ['a', 'b', 'c', 'd']
# dic = {key : val for key, val in dict.fromkeys(keys).items()}
# print(dic)

# keys = ['a', 'b', 'c', 'd']
# dic = {key : 0 for key in dict.fromkeys(keys).keys()}
# print(dic)

# dic = {'a':10, 'b':20, 'c':30, 'd':40}
# dic = {key : val for key, val in dic.items() if val != 20}
# print(dic)

# terrestrial_planet = {
#     'Mercury' : {
#         'mean_radius' : 2439.7,
#         'mass' : 3.3022E+23,
#         'orbital_period' : 87.969
#     },
#     'Venus' : {
#         'mean_radius' : 6051.8,
#         'mass' : 4.8676E+24,
#         'orbital_period' : 224.70069
#     },
#     'Earth' : {
#         'mean_radius' : 6371.0,
#         'mass' : 5.97219E+24,
#         'orbital_period' : 365.25641
#     },
#     'Mars' : {
#         'mean_radius' : 3389.5,
#         'mass' : 6.4185E+23,
#         'orbital_period' : 686.9600
#     }
# }
# print(terrestrial_planet["Venus"]['mean_radius'])

# x = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}
# y = x
# print( x is y)

# y['a'] = 90
# print(x)
# print(y)

# x = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}
# y = x.copy()
# print(x is y)

# y['a'] = 90
# print(x)
# print(y)

# x = {'a' : {'python' : '2.7'}, 'b' : {'python' : '3.6'}}
# y = x.copy()

# y['a']['python'] = '2.7.15'
# print(x)
# print(y)

# x = {'a' : {'python' : '2.7'}, 'b' : {'python' : '3.6'}}
# import copy
# y = copy.deepcopy(x)

# y['a']['python'] = '2.7.15'
# print(x)
# print(y)

# 연습문제
maria = {'korea' : 94, 'english' : 91, 'mathematics' : 89, 'science' : 83}

average = sum(maria.values()) / len(maria)
print(average)

# 연습문제
keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x.pop('delta')
x = {key : val for key, val in x.items() if val != 30}
print(x)