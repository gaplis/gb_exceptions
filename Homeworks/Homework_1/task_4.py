# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.
# Важно: При выполнении метода единственное исключение, которое пользователь может увидеть - RuntimeException.

def list_div(list_a, list_b):
    if len(list_a) != len(list_b):
        print("Длина списков не равна, будет возвращён результат по минимальному списку.")
        temp_list = None
        if len(list_a) > len(list_b):
            temp_list = list_b
        else:
            temp_list = list_a
    temp_list = list_a
    result = []
    for i in range(len(temp_list)):
        if list_b[i] == 0:
            raise Exception("В списке есть 0, на него делить нельзя")
        if type(list_b[i]) != int:
            raise Exception("В списке есть буквы")
        result.append(list_a[i] // list_b[i])
    return result


a = [1, 2, 3]
b = [5, 4, 'f']
print(list_div(a, b))