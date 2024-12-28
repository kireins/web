public class struk {
    private String productCode;
    private String productName;
    private String price;
    public struk(String productCode, String productName, String price, String amount) {
        this.productCode = productCode;
        this.productName = productName;
        this.price = price;
        this.amount = amount;
    }
    private String amount;
    public String getProductCode() {
        return productCode;
    }
    public void setProductCode(String productCode) {
        this.productCode = productCode;
    }
    public String getProductName() {
        return productName;
    }
    public void setProductName(String productName) {
        this.productName = productName;
    }
    public String getPrice() {
        return price;
    }
    public void setPrice(String price) {
        this.price = price;
    }
    public String getAmount() {
        return amount;
    }
    public void setAmount(String amount) {
        this.amount = amount;
    }
}