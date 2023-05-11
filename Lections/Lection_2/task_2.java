// ClassCastException

package Lections.Lection_2;

import java.io.File;

public class task_2 {
    public static void main(String[] args) {
        Object object = new String("123");
        File file = (File) object;
        System.out.println(file);
    }
}
