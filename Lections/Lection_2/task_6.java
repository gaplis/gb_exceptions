package Lections.Lection_2;

public class task_6 {
    public static void main(String[] args) {
        int number = 1;
        try {
            number = 10 / 1;
            String test = null;
            System.out.println(test.length());
        } catch (Exception e) {
            System.out.println("Operation divide by zero not supported");
        } 
        System.out.println(number);
    }
}
