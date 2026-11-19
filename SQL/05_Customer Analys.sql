SELECT Gender, COUNT(*) Total_Customer FROM Customer_Data_Clean.csv GROUP BY Gender;
SELECT Location, COUNT(*) Total_Customer FROM Customer_Data_Clean.csv GROUP BY Location ORDER BY Total_Customer DESC;
SELECT Subscription_Status, COUNT(*) Total_Customer FROM Customer_Data_Clean.csv GROUP BY Subscription_Status;
SELECT Payment_Method, COUNT(*) Total FROM Customer_Data_Clean.csv GROUP BY Payment_Method;
SELECT Season, AVG(Purchase_Amount_USD) Avg_Purchase FROM Customer_Data_Clean.csv GROUP BY Season;
