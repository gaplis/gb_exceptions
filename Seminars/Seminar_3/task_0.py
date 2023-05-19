try:
    with open("123.txt", "r") as reader:
        buffered_reader = reader.read()
    with open("124.txt", "w") as writer:
        writer.write(buffered_reader)
except FileNotFoundError as e:
    print(e)