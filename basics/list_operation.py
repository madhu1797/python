##list

##Declaration

list1 = [1, 2, 3]

##Accessing based on index
print(list1[0])

## Accessing based on list item
print(list1.index(3))

##Update list
list1.append(4)
print(list1)
list2 = [5, 6, 7, 8]
list1.extend(list2)
print(list1)
list1.insert(0, 0)
print(list1)
list1.append(11)

##Remove list items
list1.remove(11) #item name
list1.pop(0)    ## index
print(list1)


##sort list assending order
list1.append(0)
print(list1)
list1.sort()
print(list1)

##sort list desending order
list1.sort(reverse=True)
print(list1)


##Sorting string based list
al = ['a','d','e','c','b']
al.sort(reverse=True)
print('List in Descending Order: ', al)
al.sort()
print('List in Ascending Order: ', al)


##sorting string based list, with len the string
cities = ['Mumbai', 'London', 'Paris', 'New York']
cities.sort(key=len)
print('List in Ascending Order of the length: ', cities)

cities.sort(key=len, reverse=True)
print('List in Descending Order of the length: ', cities)
