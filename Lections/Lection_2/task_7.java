package Lections.Lection_2;

public class task_7 {
    public static void main(String[] args) {
        int number = 1;
        try {
            number = 10 / 1;
            String test = null;
            System.out.println(test.length());
        } catch (ArithmeticException e) {
            System.out.println("Operation divide by zero not supported");
        } catch (NullPointerException e) {
            System.out.println("NullPointer Exception");
        } 
        System.out.println(number);
    }
}
