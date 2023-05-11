# Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.

def request_input():
    result = input("Введите строку: ")
    if result:
        return result
    else:
        raise ValueError


while True:
    try:
        print(f"Введённая строка: {request_input()}")
        break
    except ValueError:
        print("Необходимо ввести хоть что-нибудь, попробуйте снова.")