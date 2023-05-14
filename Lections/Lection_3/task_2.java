// Создаем новое исключение

package Lections.Lection_3;

import java.io.IOException;
import java.util.Date;

public class task_2 extends IOException{
    private Date startDate;

    public task_2(String message, Date startDate, Exception e){
        super(message, e);
        this.startDate = startDate;
    }

    public Date getStartDate() {
        return startDate;
    }
}
