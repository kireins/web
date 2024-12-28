import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;



public class BillingController {
    @FXML private TextField customerNameField;
    @FXML private TextField amountField;
    @FXML private TableView<Billing> billingTable;
    @FXML private TableColumn<Billing, Integer> idColumn;
    @FXML private TableColumn<Billing, String> nameColumn;
    @FXML private TableColumn<Billing, Double> amountColumn;

    private ObservableList<Billing> billingList = FXCollections.observableArrayList();

    @FXML
    public void initialize() {
        idColumn.setCellValueFactory(cellData -> cellData.getValue().idProperty().asObject());
        nameColumn.setCellValueFactory(cellData -> cellData.getValue().nameProperty());
        amountColumn.setCellValueFactory(cellData -> cellData.getValue().amountProperty().asObject());

        loadBillingData();
    }

    @FXML
    public void handleAddBilling() {
        String name = customerNameField.getText();
        double amount = Double.parseDouble(amountField.getText());

        try (Connection conn = Database.getConnection()) {
            String query = "INSERT INTO billing (name, amount) VALUES (?, ?)";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, name);
            stmt.setDouble(2, amount);
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Insert Failed: " + e.getMessage());
        }

        customerNameField.clear();
        amountField.clear();
        loadBillingData();
    }

    private void loadBillingData() {
        billingList.clear();
        try (Connection conn = Database.getConnection()) {
            String query = "SELECT * FROM billing";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                billingList.add(new Billing(rs.getInt("id"), rs.getString("name"), rs.getDouble("amount")));
            }
        } catch (SQLException e) {
            System.err.println("Data Load Failed: " + e.getMessage());
        }

        billingTable.setItems(billingList);
    }
}
