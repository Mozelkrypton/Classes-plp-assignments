--Q1
-- Create normalized table
CREATE TABLE ProductDetail_1NF (
    OrderID INT,
    CustomerName VARCHAR(100),
    Product VARCHAR(100)
);

-- Insert atomic rows (1 product per row)
INSERT INTO ProductDetail_1NF (OrderID, CustomerName, Product) VALUES
(101, 'John Doe', 'Laptop'),
(101, 'John Doe', 'Mouse'),
(102, 'Jane Smith', 'Tablet'),
(102, 'Jane Smith', 'Keyboard'),
(102, 'Jane Smith', 'Mouse'),
(103, 'Emily Clark', 'Phone');


--Q2
-- Step 1: Create the 1NF table from Question 1 result
CREATE TABLE OrderDetails (
    OrderID INT,
    CustomerName VARCHAR(100),
    Product VARCHAR(50),
    Quantity INT,
    PRIMARY KEY (OrderID, Product)
);

-- Insert the 1NF data
INSERT INTO OrderDetails VALUES
(101, 'John Doe', 'Laptop', 2),
(101, 'John Doe', 'Mouse', 1),
(102, 'Jane Smith', 'Tablet', 3),
(102, 'Jane Smith', 'Keyboard', 1),
(102, 'Jane Smith', 'Mouse', 2),
(103, 'Emily Clark', 'Phone', 1);

-- Transform to 2NF by removing partial dependencies


-- Table 1 Orders (contains OrderID and CustomerName)
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerName VARCHAR(100)
);

-- Insert unique order-customer combinations
INSERT INTO Orders (OrderID, CustomerName)
SELECT DISTINCT OrderID, CustomerName 
FROM OrderDetails;

-- Table 2 OrderItems (contains OrderID, Product, and Quantity)
CREATE TABLE OrderItems (
    OrderID INT,
    Product VARCHAR(50),
    Quantity INT,
    PRIMARY KEY (OrderID, Product),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Insert the order items data
INSERT INTO OrderItems (OrderID, Product, Quantity)
SELECT OrderID, Product, Quantity 
FROM OrderDetails;

-- Verify 2NF structure with a query
SELECT 
    o.OrderID,
    o.CustomerName,
    oi.Product,
    oi.Quantity
FROM Orders o
JOIN OrderItems oi ON o.OrderID = oi.OrderID
ORDER BY o.OrderID, oi.Product;