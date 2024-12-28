import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ResourceBundle;
import java.net.URL;


import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;

public class DashboardController  implements Initializable{ 

    @FXML
    private Button btAdd;

    @FXML
    private ScrollPane spStruk;


    @FXML
    private TableColumn<struk, String> tcAmount;

    @FXML
    private TableColumn<struk, String> tcPrice;

    @FXML
    private TableColumn<struk, String> tcProductId;

    @FXML
    private TableColumn<struk, String> tcProductName;

    @FXML
    private TableColumn<struk, String> tcQty;

    @FXML
    private TextField tfPrice;

    @FXML
    private TextField tfPrice1;

    @FXML
    private TextField tfProductCode;

    @FXML
    private TextField tfProductName;

    @FXML
    private TableView<struk> tvProduct;


    private ObservableList<struk> strukItem = FXCollections.observableArrayList();

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        tvProduct.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);

        tcProductId.setCellValueFactory(new PropertyValueFactory<>("Product ID"));
        tcProductName.setCellValueFactory(new PropertyValueFactory<>("Product Name"));
        tcQty.setCellValueFactory(new PropertyValueFactory<>("Qty"));
        tcPrice.setCellValueFactory(new PropertyValueFactory<>("Price"));
        tcAmount.setCellValueFactory(new PropertyValueFactory<>("Amount"));

        loadTable();
    }


    public void loadTable() {
        strukItem.clear(); // Clear the list before loading new data
        Connection conn = Database.connectStrukDB();
        if (conn != null) {
            try {
                String query = "SELECT * FROM product";
                PreparedStatement stmt = conn.prepareStatement(query);
                ResultSet rslt = stmt.executeQuery();

                while (rslt.next()) {
                    strukItem.add(new struk(
                            rslt.getString("productCode"),
                            rslt.getString("productName"),
                            rslt.getString("price"),
                            rslt.getString("amount")));
                }
                tvProduct.setItems(strukItem);
            } catch (Exception e) {
                showError("Error loading data", e.getMessage());
            }
        }
    }

    public void addDataStruk() {
        if (btAdd.isPressed()) {
            Connection conn = Database.connectStrukDB();
            if (conn != null) {
                try {
                    String query = "INSERT INTO product (id, productName, price) VALUES (?, ?, ?)";
                    PreparedStatement stmnt = conn.prepareStatement(query);
                    stmnt.setString(1, tfProductCode.getText());
                    stmnt.setString(2, tfProductName.getText());
                    stmnt.setString(3, tfPrice.getText());
                    stmnt.executeUpdate();
                    showInfo("Success", "Data added successfully!");

                    clearDataStruk();
                    loadTable();
                } catch (Exception e) {
                    showError("Error adding data", e.getMessage());
                }
            }
        } else {
            showWarning("Verification Required", "Please verify the data before adding.");
        }
    }

    public void clearDataStruk() {
        tfProductCode.clear();
        tfPrice1.clear();
        tfPrice.clear();
        tfProductName.clear();
    }

     private void showError(String title, String message) {
        Alert alert = new Alert(AlertType.ERROR);
        alert.setTitle(title);
        alert.setContentText(message);
        alert.showAndWait();
    }

    private void showInfo(String title, String message) {
        Alert alert = new Alert(AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setContentText(message);
        alert.showAndWait();
    }

    private void showWarning(String title, String message) {
        Alert alert = new Alert(AlertType.WARNING);
        alert.setTitle(title);
        alert.setContentText(message);
        alert.showAndWait();
    }


}
