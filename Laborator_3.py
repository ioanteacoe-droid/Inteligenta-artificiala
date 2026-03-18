#Liste
# my_list = [1,2,"3", True]
# print(len(my_list))
# my_list.index("3")
# my_list.count(2)
#
# my_list[3]
#
# my_list[1 :]
# my_list[:1]
# my_list[-1]
# my_list[::1]
# print(my_list[::-1])
# print(my_list[0:3:2])
# #

#my_list = [1, 2, '3', True]

# print(len(my_list))
# my_list.index('3')
# my_list.count(2)
#
# print(my_list[3])
# print(my_list[1:])
# my_list[:1]
# my_list[-1]
# my_list[::1]
# my_list[::-1]
# print(my_list[0:3:2])
#
#
#
# # Add to List
# print(my_list * 2)
# print(my_list + [100])
# print(my_list + [957295912])
# my_list.append(100)
# my_list.extend([100, 200])


# Copy a List
basket = ['apples', 'pears', 'oranges']

new_basket = basket.copy()
new_basket2 = basket[:]
print(new_basket)
print(new_basket2)


 #[1, 2, 3].pop()
 #[1, 2, 3].pop(1)
 #[1, 2, 3].remove(2)
 #[1, 2, 3].clear()
# del [1, 2, 3][0]
# [1, 2, 5, 3].sort()
# [1, 2, 5, 3].sort(reverse=True)
# [1, 2, 5, 3].reverse()
# sorted([1, 2, 5, 3])
# list(reversed([1, 2, 5, 3]))
# 1 in [1, 2, 5, 3]
# min([1, 2, 3, 4, 5])
# max([1, 2, 3, 4, 5])
# sum([1, 2, 3, 4, 5])
# mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
# first, *x, last = mList
# print(first)
# print(last)

#Set
my_set = set()
print(my_set.add(1))
my_set.add(100)
my_set.add(100)
new_list = [1, 2, 3, 3, 3, 4, 4, 5, 6, 1]
print(set(new_list))
my_set.remove(100)
my_set.discard(100)
my_set.clear()
new_set = {1, 2, 3}.copy()
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.union(set2)
frozen_set = frozenset([1, 2, 3])

#dictionary
my_dict = {'name': 'John Doe', 'age': 25, 'magic_power': False}

print(my_dict['name'])
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))
list(my_dict.items())
my_dict['favourite_snack'] = 'Grapes'
my_dict.get('age')
my_dict.get('ages', 0)
del my_dict['name']
my_dict.pop('name', None)

#TUPLE
my_tuple = ('apple', 'grapes', 'mango', 'grapes')
apple, grapes_var1, mango, grapes_var2 = my_tuple
len(my_tuple)
print(my_tuple[2])
print(my_tuple[-1])

#none

type(None)
a = None
print(a)



