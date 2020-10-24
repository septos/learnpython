'''
Sets
1.Unordered
2.Unindexed
3.newset = {orange,banana,fig}
'''

new_fruits = {"lemon","fig","cherry"}
print(new_fruits)
print("-------------------------------------------------------------------------------")

#for loop
for x in new_fruits:
    print(x)
print("-------------------------------------------------------------------------------")

#add value
new_fruits.add("orange")
print(new_fruits)
new_fruits.update(["mango","grape"])
print(new_fruits)
print(len(new_fruits))
print("-------------------------------------------------------------------------------")

#remove
new_fruits.remove("fig")
print(new_fruits)

#remove = pop
x = new_fruits.pop()
print(x)
new_fruits.clear()
print(new_fruits)

