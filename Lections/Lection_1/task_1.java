package Lections.Lection_1;

import java.io.File;

public class task_1 {
    public static void main(String[] args) {
        System.out.println(getFileSize(new File("C:/Users/gapli/Downloads/gb_exceptions/Lections/Lection_1/task_1.java")));
        System.out.println(divide(10, 0));
    }

    public static int divide(int a1, int a2){
        return a1/a2;
    }

    public static long getFileSize(File file){
        if (!file.exists()) {
            return -1L;
        }
        return file.length();
    }
}
