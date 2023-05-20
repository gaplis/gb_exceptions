# Напишите приложение, которое будет запрашивать у пользователя следующие данные в произвольном порядке, разделенные пробелом:
# Фамилия Имя Отчество датарождения номертелефона пол

# Форматы данных:
# фамилия, имя, отчество - строки
# дата_рождения - строка формата dd.mm.yyyy
# номер_телефона - целое беззнаковое число без форматирования
# пол - символ латиницей f или m.

# Приложение должно проверить введенные данные по количеству. 
# Если количество не совпадает с требуемым, вернуть код ошибки, обработать его и показать пользователю сообщение, 
# что он ввел меньше и больше данных, чем требуется.
# Приложение должно попытаться распарсить полученные значения и выделить из них требуемые параметры. 
# Если форматы данных не совпадают, нужно бросить исключение, соответствующее типу проблемы. 
# Можно использовать встроенные типы java и создать свои. 
# Исключение должно быть корректно обработано, пользователю выведено сообщение с информацией, что именно неверно.
# Если всё введено и обработано верно, должен создаться файл с названием, равным фамилии, 
# в него в одну строку должны записаться полученные данные, вида
# <Фамилия><Имя><Отчество><датарождения> <номертелефона><пол>
# Однофамильцы должны записаться в один и тот же файл, в отдельные строки.
# Не забудьте закрыть соединение с файлом.
# При возникновении проблемы с чтением-записью в файл, 
# исключение должно быть корректно обработано, пользователь должен увидеть стектрейс ошибки.

class LengthException(Exception):
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return "Код ошибки 1:\n" \
                "Неверное колличество данных.\n" \
                f"Требуется 6, введено {self.length}.\n"
    
class DataFormatException(Exception):
    def __init__(self, code, data=None):
        self.data = data
        self.code = code
        self.types = {1: "10 чисел в формате 1234567890 или 11 в формате 81234567890",
                      2: "f или m",
                      3: "валидная дата в формате ДД.ММ.ГГГГ",
                      4: "Не опознан номер телефона. Необходимый формат: "
                         "10 чисел в формате 1234567890 или 11 в формате 81234567890"}

    def __str__(self):
        if self.data:
            return "Код ошибки: 2\n" \
                   "Неверный формат данных.\n" \
                   f"Требуется {self.types[self.code]}, введено {self.data}\n"
        return f"{self.types[self.code]}"
    
class ReadOnlyException(Exception):
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return "Код ошибки: 3\n" \
               f"Запись в файл {self.file_name} не удалась.\n" \



class ParseData:
    def __init__(self):
        self.text = input("""Введите текст через пробел в произвольном порядке: 
Фамилия - слово
Имя - слово
Отчество - слово
Дата рождения - ДД.ММ.ГГГГ
Номер телефона - числа без знаков и пробелов, 10 в формате 1234567890 или 11 в формате 81234567890
Пол - m или f: """).split()
        if len(self.text) != 6:
            raise LengthException(len(self.text))
        
        self.dob = self.find_dob()
        self.phone = self.find_phone()
        self.sex = self.find_sex()
        self.last_name = self.find_last_name()
        self.surname = self.find_surname()
        self.first_name = self.find_first_name()

        try:
            with open(f"{self.last_name}.txt", "a", encoding="utf-8") as file:
                file.write(f"<{self.last_name}><{self.first_name}><{self.surname}><{self.dob}><{self.phone}><{self.sex}>\n")
            print(f"Создан файл {self.last_name}")
        except PermissionError:
            raise ReadOnlyException(f"{self.last_name}.txt")
        
    def find_dob(self):
        for db in range(len(self.text)):
            if "." in self.text[db]:
                try:
                    temp = [int(j) for j in self.text[db].split(".")]
                except ValueError:
                    raise DataFormatException(3, self.text[db])
                if 0 < temp[0] <= 31 and 0 < temp[1] <= 12 and 1930 <= temp[2] <= 2023:
                    dob = self.text[db]
                    self.text.pop(db)
                    return dob
                raise DataFormatException(3, self.text[db])
            
    def find_phone(self):
        for pnum in range(len(self.text)):
            if "+" in self.text[pnum]:
                raise DataFormatException(1, self.text[pnum])
            elif self.text[pnum].isdigit():
                if len(self.text[pnum]) == 10 or (len(self.text[pnum]) == 11 and self.text[pnum][0] == "8"):
                    phone = self.text[pnum]
                    self.text.pop(pnum)
                    return phone
                raise DataFormatException(1, self.text[pnum])
            
    def find_sex(self):
        for s in range(len(self.text)):
            if len(self.text[s]) == 1:
                if self.text[s] == "f" or self.text[s] == "m":
                    sex = self.text[s]
                    self.text.pop(s)
                    return sex
                raise DataFormatException(2, self.text[s])

    def find_last_name(self):
        suffixes = ["ов", "ова", "ев", "ева", "ин", "ина", "ын", "ына", "ий", "ая", "ой"]
        for ln in self.text:
            if any(suff in ln for suff in suffixes):
                last_name = ln
                self.text.remove(ln)
                return last_name
            
    def find_surname(self):
        suffixes = ["ович", "евич", "ич", "овна", "евна", "ична", "инична"]
        for sn in self.text:
            if any(suff in sn for suff in suffixes):
                surname = sn
                self.text.remove(sn)
                return surname
            
    def find_first_name(self):
        return self.text[0]


while True:
    try:
        ParseData()
    except LengthException as e:
        print(e)
    except DataFormatException as e:
        print(e)
    except ReadOnlyException as e:
        print(e)