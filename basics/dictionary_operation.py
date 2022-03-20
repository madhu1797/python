##Declaration
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

##Accessing
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("brand"))

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)


##Updated the dictionary
thisdict["year"] = 2021
print(thisdict)

thisdict.update({"year": 2022})
print(thisdict)

##Remove the dictionary
thisdict.pop("model")
print(thisdic)



