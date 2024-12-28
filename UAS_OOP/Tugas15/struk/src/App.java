import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene; 
import javafx.stage.Stage;

public class App extends Application {


    @Override
    public void start(Stage primaryStage) throws Exception{

        Parent rootParent = FXMLLoader.load(getClass().getResource("Dashboard.fxml"));
        Scene scene = new Scene(rootParent);

        primaryStage.setTitle("Sales");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    public static void main(String[] args) throws Exception {
        launch(args);
    }
}