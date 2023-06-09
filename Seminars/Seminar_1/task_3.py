# Реализуйте метод, принимающий в качестве аргумента целочисленный двумерный массив.
# Неободимо посчитать и вернуть сумму элементов этого массива.
# При этом накладываем на метод 2 ограничения: метод может работать только с квадратными массивами (кол-во строк  = кол-ву столбцов),
# и в каждой ячейке может лежать только значение 0 или 1.
# Если нарушается одно из условий, метод должен бросить RuntimeException с сообщением об ошибке.

def array_sum(array):
    result = 0
    for i in range(len(array)):
        if len(array) != len(array[i]):
            raise Exception("Массив не квадратный!")
        for j in range(len(array[i])):
            if array[i][j] == 0 or array[i][j] == 1:
                result += array[i][j]
            else:
                raise Exception("В массиве должны быть только 0 и 1.")
    return result

array = [[1, 1, 0], [0, 0, 1], [0, 1, 1]]
print(array_sum(array))