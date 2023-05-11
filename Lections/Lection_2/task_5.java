package Lections.Lection_2;

public class task_5 {
    public static void main(String[] args) {
        int number = 1;
        try {
            number = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Operation divide by zero not supported");
        }
        System.out.println(number);
    }
}
