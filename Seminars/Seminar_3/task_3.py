# 1. Создайте класс исключения, который будет выбрасываться при делении на 0. 
#    Исключение должно отображать понятное для пользователя сообщение об ошибке.
# 2. Создайте класс исключений, которое будет возникать при обращении к пустому элементу в массиве ссылочного типа. 
#    Исключение должно отображать понятное для пользователя сообщение об ошибке.
# 3. Создайте класс исключения, которое будет возникать при попытке открыть несуществующий файл.
#    Исключение должно отображать понятное для пользователя сообщение об ошибке.

import os


class DivisionByZeroError(ArithmeticError):
    pass


class NullElementError(TypeError):
    pass


class FileNotExists(FileNotFoundError):
    pass


def division(a, b):
    if b == 0:
        raise DivisionByZeroError
    else:
        return a / b


def array_elem(arr, ind):
    if arr[ind]:
        return arr[ind]
    raise NullElementError


def check_file(path):
    if os.path.exists(path):
        return os.path.exists(path)
    raise FileNotExists


lst = [1, 2, 3, None, 5, None, 0]
try:
    # division(2, 0)
    # array_elem(lst, 3)
    print(check_file("1235.txt"))
except DivisionByZeroError:
    print("Нельзя делить на ноль!")
except NullElementError:
    print("Пустой элемент")
except FileNotExists:
    print("Файла не существует!")