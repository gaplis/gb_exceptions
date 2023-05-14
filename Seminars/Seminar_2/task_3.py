# Запишите в файл следующие строки:
# Анна=4
# Елена=5
# Марина=6
# Владимир=?
# Константин=?
# Иван=4
# Реализуйте метод, который считывает данные из файла и сохраняет в двумерный массив (либо HashMap, если студенты с ним знакомы).
# В отдельном методе нужно будет пройти по структуре данных, если сохранено значение ?, заменить его на соответствующее число.
# Если на какому-то месте встречается символ, отличный от числа или ?, бросить подходящее исключение.
# Записать в тот же файл данные с заменёнными символами ?.

def read_file():
    with open("task_3.txt", "r", encoding="utf-8") as file:
        file = file.readlines()
        result = {}
        for i in file:
            try:
                key, value = i.strip().split("=")
                if (not value.isdigit()) and value != "?":
                    continue
            except ValueError as e:
                print(f"Некорректная строка: '{i.strip()}' удалена из массива.")
            result[key] = value
    return result


def check_file(file):
    for key in file.keys():
        if file[key] == "?":
            file[key] = len(key)
    return file


def write_file(file):
    file = [f"{key}={file[key]}\n" for key in file.keys()]
    with open("task_3.txt", "w", encoding="utf-8") as f:
        f.writelines(file)


text = read_file()
text = check_file(text)
write_file(text)