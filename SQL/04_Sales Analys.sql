SELECT Category, SUM(List_Price*Quantity) Revenue FROM Order_Data_Clean.csv GROUP BY Category ORDER BY Revenue DESC;
SELECT Category, SUM((List_Price-Cost_Price)*Quantity) Profit FROM Order_Data_Clean.csv GROUP BY Category ORDER BY Profit DESC;
SELECT Product_ID, SUM(List_Price*Quantity) Revenue FROM Order_Data_Clean.csv GROUP BY Product_ID ORDER BY Revenue DESC LIMIT 10;
SELECT Category, SUM(Quantity) Total_Quantity FROM Order_Data_Clean.csv GROUP BY Category ORDER BY Total_Quantity DESC;
SELECT Ship_Mode, COUNT(*) Total_Order FROM Order_Data_Clean.csv GROUP BY Ship_Mode ORDER BY Total_Order DESC;
SELECT Category, AVG(Discount_Percent) Avg_Discount FROM Order_Data_Clean.csv GROUP BY Category;