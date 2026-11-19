SELECT
    c.Customer_ID,
    c.Gender,
    c.Location,
    o.Order_ID,
    o.Category,
    o.Sub_Category,
    o.Quantity
FROM Customer_Data_Clean.csv c
INNER JOIN Order_Data_Clean.csv o
ON c.Customer_ID = o.Customer_ID;

SELECT
    c.Location,
    SUM(o.List_Price * o.Quantity) AS Revenue
FROM Customer_Data_Clean.csv c
JOIN Order_Data_Clean.csv o
ON c.Customer_ID = o.Customer_ID
GROUP BY c.Location
ORDER BY Revenue DESC;

SELECT
    c.Location,
    SUM(o.List_Price * o.Quantity) AS Revenue
FROM Customer_Data_Clean.csv c
JOIN Order_Data_Clean.csv o
ON c.Customer_ID = o.Customer_ID
GROUP BY c.Location
ORDER BY Revenue DESC;

SELECT
    Customer_ID,
    Age,
    CASE
        WHEN Age < 25 THEN 'Young'
        WHEN Age BETWEEN 25 AND 40 THEN 'Adult'
        ELSE 'Senior'
    END AS Age_Group
FROM Customer_Data_Clean.csv; 

WITH Revenue AS
(
    SELECT
        Category,
        SUM(List_Price * Quantity) AS Revenue
    FROM Order_Data_Clean.csv
    GROUP BY Category
)

SELECT *
FROM Revenue
ORDER BY Revenue DESC;

SELECT
    Category,
    SUM(List_Price * Quantity) AS Revenue,
    RANK() OVER(
        ORDER BY SUM(List_Price * Quantity) DESC
    ) AS Ranking
FROM Order_Data_Clean.csv
GROUP BY Category;

SELECT
    Category,
    SUM(List_Price * Quantity) AS Revenue,
    DENSE_RANK() OVER(
        ORDER BY SUM(List_Price * Quantity) DESC
    ) AS Rank_Category
FROM Order_Data_Clean.csv
GROUP BY Category;

SELECT
    Order_ID,
    Order_Date,
    ROW_NUMBER() OVER(
        ORDER BY Order_Date
    ) AS Row_Num
FROM Order_Data_Clean.csv;

SELECT
    Product_ID,
    SUM(List_Price * Quantity) AS Revenue
FROM Order_Data_Clean.csv
GROUP BY Product_ID
HAVING Revenue >
(
    SELECT AVG(List_Price * Quantity)
    FROM Order_Data_Clean.csv
)
ORDER BY Revenue DESC;

SELECT
    Order_Date,
    SUM(List_Price * Quantity) AS Revenue,
    SUM(SUM(List_Price * Quantity))
        OVER(ORDER BY Order_Date) AS Running_Total
FROM Order_Data_Clean.csv
GROUP BY Order_Date;

