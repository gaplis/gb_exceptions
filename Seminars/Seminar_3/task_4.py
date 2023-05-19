# 1. Напишите метод, на вход которого подаётся двумерный строковый массив размером 4х4.
#    При подаче массива другого размера необходимо бросить исключение MyArraySizeException.
# 2. Далее метод должен пройтись по всем элементам массива, преобразовать в int и просуммировать.
#    Если в каком-то элементе массива преобразование не удалось (например, в ячейке лежит символ или текст вместо числа),
#    должно быть брошено исключение MyArrayDataException с детализацией, в какой именно ячейке лежат неверные данные.
# 3. В методе main() вызвать полученный метод обработать возможные исключения MyArraySizeException и MyArrayDataException
#    и вывести результат расчета (сумму элементов, при условии что подали на вход корректный массив).

class MyArraySizeException(IndexError):
    pass


class MyArrayDataException(Exception):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f"Неверный элемент в {self.row + 1} строке и {self.col + 1} столбце"


def sum_array(arr):
    summ = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if len(arr) != len(arr[i]):
                raise MyArraySizeException
            if isinstance(arr[i][j], str):
                if arr[i][j].isdigit():
                    summ += int(arr[i][j])
                else:
                    raise MyArrayDataException(i, j)

            else:
                raise MyArrayDataException(i, j)
    return summ


array = [["1", "0", "3", "1"], ["4", "5", "6", "7"], ["7", "8", "9", "10"], ["11", "12", "13", "14"]]
try:
    print(sum_array(array))
except MyArraySizeException:
    print("Массив не квадратный")
except MyArrayDataException as e:
    print(e)