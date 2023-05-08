# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения

def divide(a, b):
    return a / b


def string_to_int(text):
    return int(text)


def file_not_found(filename):
    with open(filename, "r") as f:
        return f.read()
    
print(divide(10, 0))
print(string_to_int("text"))
print(file_not_found("1.txt"))
