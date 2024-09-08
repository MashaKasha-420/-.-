#  работа со словарями
my_dict = {'Maria': 2002, 'Ivan': 1992, 'Katya': 2000 }
print(my_dict)

print(my_dict['Maria'])
my_dict['Alisa']=2020
print(my_dict['Alisa'])

my_dict.update({'Helena': 1980, 'Polina':2004})

my_dict.pop('Maria')
#a  =  my_dict.pop('Maria') # хотя я вроде делала все по лекции, значение   от ключа  не выводится и выдает ошибку
#print(a)
print(my_dict)

#  работа с множествами
my_set = {1, 1, 5, 'str', 2, 5, 3, False, 'str',  False}
print(my_set)


my_set.discard(1)
my_set.update([4, True])
print(my_set)