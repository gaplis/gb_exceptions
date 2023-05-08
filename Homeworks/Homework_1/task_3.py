# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.

def list_diff(list_a, list_b):
    if len(list_a) != len(list_b):
        print("Длина списков не одинаковая, будет возвращён результат по минимальному списку.")
        temp_list = None
        if len(list_a) > len(list_b):
            temp_list = list_b
        else:
            temp_list = list_a
    temp_list = list_a
    result = []
    for i in range(len(temp_list)):
        result.append(list_a[i] - list_b[i])
    return result


a = [1, 2, 3]
b = [5, 4, 3]
print(list_diff(a, b))