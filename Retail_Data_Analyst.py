# ==========================================
# IMPORT LIBRARY
# ==========================================
import pandas as pd 
import matplotlib.pyplot as plt
# ==========================================
# LOAD DATASET
# ==========================================
customer = pd.read_csv("data/Customer_Data.csv")
order = pd.read_csv("data/Order_Data.csv")
# ==========================================
# DATA UNDERSTANDING
# ==========================================
#5 dataset awal
print("===== CUSTOMER DATA =====")
print(customer.head())
print("\n===== ORDER DATA =====")
print(order.head())

#informasi dataset
print("\n===== CUSTOMER INFO =====")
customer.info()
print("\n===== ORDER INFO =====")
order.info()

#melihat ukuran dataset
print("\n===== CUSTOMER SHAPE =====")
print(customer.shape)
print("\n===== ORDER SHAPE =====")
print(order.shape) 
# ==========================================
# MISSING VALUE
# ==========================================
#jumlah baris yg hilang di setiap kolom
print("\n===== Missing Value Customer =====")
print(customer.isnull().sum())
print("\n===== Missing Value Order =====")
print(order.isnull().sum()) 
# ==========================================
# DUPLICATE DATA
# ==========================================
print("\n===== Duplicate Customer =====")
print(customer.duplicated().sum())
print("\n===== Duplicate Order =====")
print(order.duplicated().sum()) 

#nama kolom
print("\n===== Customer Columns =====")
print(customer.columns)
print("\n===== Order Columns =====")
print(order.columns) 

print("\n===== DESCRIPTIVE STATISTICS - ORDER DATA =====")
print(order.describe()) 
print("\nDETAIL DUPLICATE CUSTOMER")
print(customer[customer.duplicated()])
# ==========================================
# MISSING VALUE DETAIL
# ==========================================
print("\nMISSING VALUE - PURCHASE AMOUNT")
print(customer[customer["Purchase Amount (USD)"].isnull()].head()) 

print("\nMISSING VALUE - SIZE")
print(customer[customer["Size"].isnull()].head())

print("\nMISSING VALUE - REVIEW RATING")
print(customer[customer["Review Rating"].isnull()].head()) 

print("\nMISSING VALUE - DISCOUNT APPLIED")
print(customer[customer["Discount Applied"].isnull()]) 

print("\nMISSING VALUE - PREVIOUS PURCHASES")
print(customer[customer["Previous Purchases"].isnull()].head())

print("\nMISSING VALUE SHIP MODE")
print(order[order["Ship Mode"].isnull()])

print("\n===== CUSTOMER DATA TYPES =====")
print(customer.dtypes)
print("\n===== ORDER DATA TYPES =====")
print(order.dtypes) 
# ==========================================
# DATA CLEANING
# ==========================================
# RENAME COLUMN
order.rename(columns={
    "Order Id": "Order_ID",
    "Order Date": "Order_Date",
    "Ship Mode": "Ship_Mode",
    "Sub Category": "Sub_Category",
    "Product Id": "Product_ID",
    "cost price": "Cost_Price",
    "List Price": "List_Price",
    "Discount Percent": "Discount_Percent",
    "Customer ID": "Customer_ID"
}, inplace=True)

customer.rename(columns={
    "Customer ID": "Customer_ID",
    "Purchase Amount (USD)": "Purchase_Amount_USD",
    "Review Rating": "Review_Rating",
    "Subscription Status": "Subscription_Status",
    "Discount Applied": "Discount_Applied",
    "Previous Purchases": "Previous_Purchases",
    "Payment Method": "Payment_Method",
    "Frequency of Purchases": "Frequency_of_Purchases"
}, inplace=True) 

print("\n===== AFTER RENAME =====")
print(order.columns)
print(customer.columns)

# Samakan separator tanggal agar format konsisten
order["Order_Date"] = order["Order_Date"].str.replace("-", "/", regex=False)

# Mengubah tipe data Order_Date menjadi datetime
order["Order_Date"] = pd.to_datetime(
    order["Order_Date"],
    dayfirst=True
)

print("\n===== ORDER DATA TYPES AFTER CONVERT =====")
print(order.dtypes)
print("\n===== CUSTOMER DATA TYPES AFTER CLEANING =====")
print(customer.dtypes) 
# ==========================================
# HANDLE MISSING VALUE - CUSTOMER DATA
# ==========================================
customer["Purchase_Amount_USD"] = customer["Purchase_Amount_USD"].fillna(
    customer["Purchase_Amount_USD"].median()
)

customer["Size"] = customer["Size"].fillna(
    customer["Size"].mode()[0]
)

customer["Review_Rating"] = customer["Review_Rating"].fillna(
    customer["Review_Rating"].median()
)

customer["Discount_Applied"] = customer["Discount_Applied"].fillna(
    customer["Discount_Applied"].mode()[0]
)

customer["Previous_Purchases"] = customer["Previous_Purchases"].fillna(
    customer["Previous_Purchases"].median()
)
# ==========================================
# HANDLE MISSING VALUE - ORDER DATA
# ==========================================
order["Ship_Mode"] = order["Ship_Mode"].fillna(
    order["Ship_Mode"].mode()[0]
)
# ==========================================
# CHECK MISSING VALUE AFTER CLEANING
# ==========================================
print("\n===== CUSTOMER MISSING VALUE AFTER CLEANING =====")
print(customer.isnull().sum())

print("\n===== ORDER MISSING VALUE AFTER CLEANING =====")
print(order.isnull().sum()) 
# ==========================================
# HANDLE DUPLICATE DATA
# ==========================================
print("\n===== DUPLICATE CUSTOMER DETAIL =====")
print(customer[customer.duplicated(keep=False)])
# Duplicate customer memiliki seluruh nilai yang identik,
# sehingga aman untuk dihapus.
customer.drop_duplicates(inplace=True)

customer.reset_index(drop=True, inplace=True)

print("\n===== DUPLICATE CUSTOMER AFTER CLEANING =====")
print(customer.duplicated().sum()) 

print("\n===== FINAL DATASET SHAPE =====")
print("Customer :", customer.shape)
print("Order    :", order.shape)
# ==========================================
# OUTLIER DETECTION
# ==========================================
customer_numeric = [
    "Age",
    "Purchase_Amount_USD",
    "Review_Rating",
    "Previous_Purchases"
]

for col in customer_numeric:
    plt.figure(figsize=(6, 3))
    plt.boxplot(customer[col])
    plt.title(f"Boxplot of {col}")
    plt.show() 

order_numeric = [
    "Cost_Price",
    "List_Price",
    "Quantity",
    "Discount_Percent"
]

for col in order_numeric:
    plt.figure(figsize=(6,3))
    plt.boxplot(order[col])
    plt.title(f"Boxplot of {col}")
    plt.show() 
# Berdasarkan hasil boxplot,
# outlier tidak dihapus karena masih merepresentasikan
# variasi transaksi yang valid.

# ==========================================
# EXPORT CLEAN DATASET
# ==========================================
customer.to_csv("data/Customer_Data_Clean.csv", index=False)
order.to_csv("data/Order_Data_Clean.csv", index=False)
print("\n===== DATASET BERHASIL DISIMPAN =====")
print("Customer_Data_Clean.csv")
print("Order_Data_Clean.csv") 

#==========================================
# EXPLORATORY DATA ANALYST (EDA)
#==========================================
print("\n======== DESCRIPTIVE STATISTICS - CUSTOMER ==========")
print(customer.describe())

print("\n======== GENDER DISTRIBUTION ==========")
print(customer["Gender"].value_counts())

print("\n======== AGE DISTRIBUTION ==========")
print(customer["Age"].describe())

print("\n========= LOCATION DISTRIBUTION ========")
print(customer["Location"].value_counts())

print("\n========= SEASON DISTIBUTION ===========")
print(customer["Season"].value_counts())

print("\n======== PAYMENT DISTRIBUTION ==========")
print(customer["Payment_Method"].value_counts())

print("\n======== SUBCRIPTION STATUS DISTRIBUTION ==========")
print(customer["Subscription_Status"].value_counts())

print("\n======== PURCHASE AMOUNT DISTRIBUTION ==========")
print(customer["Purchase_Amount_USD"].describe()) 

print("\n======== PREVIOUS PURCHASE DISTRIBUTION ==========")
print(customer["Previous_Purchases"].describe())

print("\n======== FREQUENCY OF PURCHASES DISTRIBUTION ==========")
print(customer["Frequency_of_Purchases"].value_counts())

print("\n======== DISCOUNT DISTRIBUTION ==========")
print(customer["Discount_Applied"].value_counts())


print("\n======== DESCRIPTIVE STATISTICS - ORDER ==========")
print(order.describe())

print("\n======== DATE RANGE ==========")
print(order["Order_Date"].min())
print(order["Order_Date"].max())

print("\n======== SHIP MODE DISTRIBUTION ==========")
print(order["Ship_Mode"].value_counts())

print("\n======== SEGMENT DISTRIBUTION ==========")
print(order["Segment"].value_counts())

print("\n======== CATEGORY DISTRIBUTION ==========")
print(order["Category"].value_counts())

print("\n======== SUB CATEGORY ==========")
print(order["Sub_Category"].value_counts())

print("\n======== QUANTITY DISTRIBUTION ==========")
print(order["Quantity"].describe())

print("\n======== DISCOUNT DISTRIBUTION ==========")
print(order["Discount_Percent"].value_counts())

order["Revenue"] = order["List_Price"] * order["Quantity"]

print("\n======== TOTAL REVENUE ==========")
print(order["Revenue"].sum())

print("\n======== REVENUE STATISTICS ==========")
print(order["Revenue"].describe())