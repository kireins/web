import java.sql.Connection;
import java.sql.DriverManager;

public class Database {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/strukDB";
    private static final String DB_USER = "root";
    private static final String DB_PASS = "";

    public static Connection connectStrukDB(){
        try {
            return DriverManager.getConnection(DB_URL,DB_USER,DB_PASS);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
