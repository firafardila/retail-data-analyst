SELECT SUM(List_Price*Quantity) AS Total_Revenue FROM Order_Data_Clean.csv;
SELECT SUM((List_Price-Cost_Price)*Quantity) AS Total_Profit FROM Order_Data_Clean.csv;
SELECT AVG(List_Price*Quantity) AS Average_Order_Value FROM Order_Data_Clean.csv;
SELECT SUM(Quantity) AS Total_Quantity FROM Order_Data_Clean.csv;
