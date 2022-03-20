"""
NOTE:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""
#Declaration-1

myset = {"apple", "banana", "cherry"}
print(myset)


#Declaration-2
set2 = set(("apple", "banana", "cherry"))
print(set2)

##Change Items:  Once a set is created, you cannot change its items, but you can add new items.

##Accessing sets:
for x in set2:
  print(x)

##Add items: Once a set is created, you cannot change its items, but you can add new items.
set2.add("orange")
print(set2)

##To add items from another set into the current set
tropical = {"pineapple", "mango", "papaya"}
set2.update(tropical)
print(set2)

##REMOVE
##To remove an item in a set, use the remove(), or the discard() method.
##If the item to remove does not exist, remove() will raise an error.
##If the item to remove does not exist, discard() will NOT raise an error.
##pop() method to remove an item, but this method will remove the last item.
##clear() method empties the set:

set2.remove("banana")
print(set2)
set2.discard("banana")
print(set2)
set2.pop()
print(set2)
set2.clear()
print(set2)

##del keyword will delete the set completely
del set2
#print(set2)


