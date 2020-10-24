'''
dictionary is 
1.unordered (tidak berurutan)
2.changeable(isinya bisa diganti, 
3.indexed(bisa diurutkan berdasarkan no index),
aturannya pakai breket
{key1: value1, key2: value2}
'''

# #1 dict methode
# player_number = {'messi':10, 'ronaldo':7, 'salah:':11}
# print(player_number)

#2 dict methode2
fruits_price = {'Apple': 5, 'banana': 4, 'fig': 3}

print(fruits_price['Apple'])
print(fruits_price.get('banana'))   #('key')

price = {'Rupiah':[5000, 10000, 20000, 50000, 100000], 'Dollar': 2, 'Dirham':10}
print(price['Rupiah'][2])


print("-----------------------------------------------------------------------------------------")
#update dictionary, add new value, del key
#update data
player_age = {"L. Suárez": 33, "K. De Bruyne": 29, "Bruno Fernandes": 25}
player_age["L. Suárez"] = 30
print(player_age)
#add new value
player_age["A. Griezmann"] = 29
print(player_age)
#delete 
del player_age["Bruno Fernandes"]
print(player_age)
