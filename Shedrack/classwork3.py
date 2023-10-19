# Q1. Create an empty dictionary
mydict = {}
print(mydict)
# Q2. Use a method to add a new value for the key "name"
mydict.update({'name': 'Shedrack Yusuf'})
print(mydict)
# Q3. Create a new variable and store a tuple of the current key value pair from our dictionary
#     such that the dictionary now becomes empty.
x = ('name', 'Alameen Bature')
mydict.clear()
print(mydict)
# Q3. Use the appropraite method to update the dictionary back to its original form using our
#     new variable holding its original values
mydict.setdefault('name', x[1])
print(mydict)
# Q4. Use the right method to get and print out the "name" from the restored dictionary
print(mydict.get('name'))
# Q5. Using operation similar to list, add values for each of the following keys into th dictionary:
#       - "age". "height". "weight", "hobbies"
mydict['age'] = 70
mydict['height'] = 6.0
mydict['weight'] = 56.5
mydict['hobbies'] = "Dancing", "Drawing", "WorkOut"
print(mydict)
# Q6. Create a new variable to store the value returned from removing hobbies
y = mydict.popitem() 
print(y)
# Q7. Use the appropraite method to remove all items from the dictionary
mydict.clear()
print(mydict)
# Q8. Repeat Q2-Q6 here
mydict.update({'name': 'Shedrack Yusuf'})
print(mydict)

z = ("name", "Bose Oladimeji")
mydict.clear()
print(mydict)

mydict.setdefault('name', z[1])
print(mydict)

print(mydict.get("name"))

mydict['age'] = 23
mydict['height'] = 1.5
mydict['weight'] = 78.9
mydict['hobbies'] = "Reading", "Dancing", "Singing"
print(mydict)

k = mydict.popitem()
print(k)

mydict.clear()
print(mydict)