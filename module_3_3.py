#Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True)
def print_params (a: object = 1, b: object = 'строка', c: object = True):
    print(a, b, c)

#Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(1),
print_params(2, '2')
print_params(3, 'Анатолий', False)
#Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = '25')
print_params(c =[1, 2, 3])

#Создайте список values_list с тремя элементами разных типов.
values_list = [ 'строка', 33.3, True]
values_dict = {'a': 33, 'b':  'строка', 'c': False}

#Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря)
print_params(*values_list)
print_params(**values_dict)

#Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [54.32, 'Строка']

#Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)

