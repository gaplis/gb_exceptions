package Lections.Lection_1;

public class task_2 {
    public static void main(String[] args) {
        a();
    }

    public static void a(){
        b();
    }

    public static void b(){
        c();
    }

    public static void c(){
        int[] ints = new int[10];
        System.out.println(ints[1000]);
    }
}
