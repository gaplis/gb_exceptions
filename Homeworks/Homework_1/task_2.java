// Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?

package Homeworks.Homework_1;

public class task_2 { 

    public static int sum2d(String[][] arr){
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < 5; j++) {
                int val = Integer.parseInt(arr[i][j]);
                sum += val;
            }
        }
    }
}

// В 7 строке метод должен возвращать int значение, а возвратов никаких нет
// В 10 строке длина массива может быть меньше 5
// В 11 строке может возникнуть ошибка преобразования строки в число, так как могут быть и буквы