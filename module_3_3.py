#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params() # вызов без аргументов работает  т.к параметры  функц. именованные

print_params(1,2,3) # вызов работает, значание параметров переопределилось

print_params(b = 25) # вызов работает, значение  'b' переопределилось

print_params(8, 9, c = [1,2,3]) # вызов работает, значение  'c' изменилось  именованно, а 'a' и'b' позиционо


#2.Распаковка параметров:
values_list =  [3, True, 'Hello']
values_dict  = {'a':False, 'b':6, 'c':'String'}


print_params(*values_list)

print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [9, '9']

print_params(*values_list_2, 42) # вызов работает, 2 эл. списка встали как a и b, с изменила значение на 42