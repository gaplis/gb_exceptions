/*Реализуйте метод, принимающий в качестве аргумента целочисленный массив.
Если длинна массива меньше некоторого заданного минимума, метод возвращает -1, в качестве кода ошибки, иначе - длину массива. */

package Seminars.Seminar_1;

public class task_1 {
    private static int MIN_LENGTH_ARRAY =  5;

    public static void main(String[] args) {
        int[] array = new int[]{1,2,3,4,5,6,7,8,9,5};
        int[] array2 = new int[]{1,2,3};
        System.out.println(getLengthArray(array));
        System.out.println(getLengthArray(array2));
    }

    private static int getLengthArray(int[] array){
        if (array.length < MIN_LENGTH_ARRAY) {
            return -1;
        }
        return array.length;
    }
}
