def sum2d(arr):
    summ = 0
    for i in range(len(arr)):
        for j in range(5):
            try:
                summ += int(arr[i][j])
            except ValueError:
                continue
            except IndexError:
                break
    return summ


array = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
print(sum2d(array))