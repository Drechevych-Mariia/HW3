int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a),id(str_b),id(set_c),id(lst_d),id(dict_e))

lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

print(type(int_a),type(str_b),type(set_c),type(lst_d),type(dict_e))

print(isinstance(int_a,int),isinstance(str_b,str),isinstance(set_c,set),isinstance(lst_d,list),isinstance(dict_e,dict))

print("Anna has {} apples and {} peaches.".format(10,20))

print("Anna has {1} apples and {0} peaches.".format(10,20))

print("Anna has {apples} apples and {peaches} peaches.".format(apples=10, peaches=20))

print("Anna has {0:5} apples and {1:3} peaches.".format(10,20))

apples =1
peaches =2
print(f"Anna has {apples} apples and {peaches} peaches.")

Apples = 1
Peaches = 7
print("Anna has %s apples and %d peaches." % (Apples, Peaches))

dict = {"a": apples, "p": peaches}
print("Anna has %(a)s apples and %(p)s peaches" % dict)

lst_comp1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comp1)

lst_comp2 = []
for num in range(10):
    if num % 2 == 0:
        lst_comp2.append(num // 2)
    else:
        lst_comp2.append(num *10)
print(lst_comp2)

dict_comp3 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comp3)

dict_comp4 = {num: num ** 2 if num % 2 == 1 else num // 0.5  for num in range (1, 11)}
print (dict_comp4)

dict_comp5 = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comp5[x] = x**3
print(dict_comp5)

dict_comp6 = {}
for x in range(10):
    dict_comp6[x] = (
        x ** 3
        if x ** 3 % 4 == 0
        else x
    )
print(dict_comp6)

x = 1
y = 2
foo = lambda x, y: x if x < y else y
print(foo(x,y))

x = 1
y = 2
z = 3
def foo (x,y,z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(x,y,z))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(lst_to_sort)

lst_to_sort.sort(reverse=True)
print(lst_to_sort)

lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(lst_to_sort)

list_A = [2, 3, 4]
list_B = [5, 6, 7]
raised_list_A = list(map(lambda a, b: a ** b, list_A, list_B))
print(raised_list_A)

from functools import reduce
sum = reduce(lambda x, y: x + y, lst_to_sort)
print(sum)

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
new_lst2 = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(new_lst2)

b = range(-10, 10)
print('Filter negative numbers:', list(filter(lambda x: x < 0, b)))

list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
new_lst3 = list(filter(lambda num: num in list_1, list_2))
print(new_lst3)