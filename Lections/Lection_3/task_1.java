package Lections.Lection_3;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class task_1 {
    public static void main(String[] args) {
        try (FileReader reader = new FileReader("C:/Users/gapli/Downloads/gb_exceptions/Lections/Lection_3/task_1.txt");
            FileWriter writer = new FileWriter("test_1.txt")) {
                while (reader.ready()){
                    writer.write(reader.read());
                }
        } catch (RuntimeException | IOException e) {
            System.out.println("Catch exception: " + e.getClass().getSimpleName());
        }
        System.out.println("Copy successfully");

        try {
            System.out.println("Test operation");
        } finally {
            System.out.println("Finally operation");
        }
    }
}
