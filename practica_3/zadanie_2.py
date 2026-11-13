#1
my_list = [1, 2, 3]
print(my_list)
my_list[0]=100
print(my_list)

#2
my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple[0]=100 #будет ошибка потому что неизменяемый тип данных
print(my_tuple)

#3
my_string = "cat"
print(my_string)
my_string[0] = 'b' #тоже будет ошибка потому что неизменяемый тип данных
print(my_string)
