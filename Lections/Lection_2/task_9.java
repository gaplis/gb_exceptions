package Lections.Lection_2;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class task_9 {
    public static void main(String[] args) throws IOException {
        FileReader test = null;
        try {
            test = new FileReader("test");
            test.read();
        } catch(RuntimeException | IOException e){
            System.out.println("Catch exception: " + e.getClass().getSimpleName());
        } finally {
            System.out.println("Finally start.");
            if (test != null) {
                try {
                    test.close();
                } catch (IOException e) {
                    System.out.println("Exception while close.");
                }
            }
            System.out.println("Finally finished.");
        }
    }
}
