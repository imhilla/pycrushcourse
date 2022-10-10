# changing, adding, removing
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# adding element
motorcycles.append('ducati')
print(motorcycles)

empty_cycle_list = []
empty_cycle_list.append('honda')
empty_cycle_list.append('suzuki')
empty_cycle_list.append('ducati')
empty_cycle_list.append('yamaha')
print(empty_cycle_list)

# inserting a list
# you can add a new element at any position in your list by using insert()
empty_cycle_list.insert(0, "taro")
print(empty_cycle_list)

# removing elemnts from the list
# remove using del cmd
del empty_cycle_list[0]
print(empty_cycle_list)

# removing an item using pop()

popped_cycle = empty_cycle_list.pop()
print(popped_cycle)

# poping items from any position
# by including index of the item in parenthesis

popped_cycle = empty_cycle_list.pop(1)
print(popped_cycle)


# removing an item by value
# if you kno the value of the item to remove you can use the remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

print(motorcycles.remove('honda'))
print(motorcycles)
