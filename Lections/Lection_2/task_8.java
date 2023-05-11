package Lections.Lection_2;

import java.io.FileNotFoundException;
import java.io.FileReader;

public class task_8 {
    public static void main(String[] args) {
        try {
            FileReader test = new FileReader("test");
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}
