arr = [0 for _ in range(10)]
while True:
    try:
        index = int(input("Укажите индекс элемента массива, в который хотите записать значение 1: "))
        arr[index] = 1
        print(arr)
    except ValueError:
        print("Должно быть введено число!")
    except IndexError:
        print("Указан индекс за пределами списка!")