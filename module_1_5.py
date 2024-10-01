immutable_var = (1, 2, 3, 'hello', True)
print(immutable_var)
#immutable_var[0] = 100500 #Кортеж нельзя изменить, в него можно добавить значения, мо мыожем заменить элементы внутр списка в кортеже

#immutable_var = ([1, 2, 3], 'hello', True) #Это как пример, что можно заменить в коретеже
#immutable_var[0][0] = 4
#print(immutable_var)

mutable_list = ['one', 'two', 'three']
print(mutable_list)
mutable_list[0:3] = 'asd', 'qwer', 'momo', 'ssww'
print(mutable_list)