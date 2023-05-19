# Создайте метод doSomething(), который может быть источником одного из типов checked exceptions (тело самого метода прописывать не обязательно).
# Вызовите метод из main и обработайте в нем исключение, которое вызвал метод doSomething().

def do_something(a, b):
    return a / b


try:
    result = do_something(2, 0)
except ZeroDivisionError:
    print("Error")
else:
    print(result)