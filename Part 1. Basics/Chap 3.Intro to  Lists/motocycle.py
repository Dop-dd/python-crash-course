motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#['honda', 'yamaha', 'suzuki']

""" change the first valie of the item """

motorcycles[0] = "ducati"
print(motorcycles)
# ['ducati', 'yamaha', 'suzuki']

""" append elements """
motorcycles.append('kawasaki')
print(motorcycles)
# ['ducati', 'yamaha', 'suzuki', 'kawasaki']

""" Inserting Elements into a List """
# You can add a new element at any position in your list by using the insert()
# method. You do this by specifying the index of the new element and the
# value of the new item.
motorcycles.insert(1, 'bugati')
print(motorcycles)
# ['ducati', 'bugati', 'yamaha', 'suzuki', 'kawasaki']

""" Removing Elements from a List """
motorcycles = ['ducati', 'bugati', 'yamaha', 'suzuki', 'kawasaki']
del motorcycles[3]
print(motorcycles)
# ['ducati', 'bugati', 'yamaha', 'kawasaki'] - suzuki at positon 3 is deleted