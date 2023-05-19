# Создайте класс Счетчик, у которого есть метод add(), увеличивающий значение внутренней int переменной на 1.
# Сделайте так, чтобы с объектом такого типа можно было работать в блоке try-with-resources. 
# Подумайте, что должно происходить при закрытии этого ресурса? Напишите метод для проверки, закрыт ли ресурс.
# При попытке вызвать add() у закрытого ресурса, должен выброситься IOException.

class Counter:
    count = 0
    path = "123.txt"
    file = None

    def open(self):
        self.file = open(self.path, "a")

    def close(self):
        self.file.close()

    def add(self):
        try:
            self.file.write(str(self.count))
            self.count += 1
        except ValueError:
            print("File is closed")


add_count = Counter()
add_count.open()
add_count.add()
add_count.close()
# add_count.open()
add_count.add()