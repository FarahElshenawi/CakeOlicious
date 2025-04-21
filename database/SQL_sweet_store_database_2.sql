CREATE TABLE Cart (
  id INT PRIMARY KEY IDENTITY(1,1),
  user_id INT NOT NULL FOREIGN KEY REFERENCES users(id),
  product_id INT NOT NULL FOREIGN KEY REFERENCES products(id),
  quantity INT NOT NULL CHECK (Quantity > 0),
  price DECIMAL(10, 2) NOT NULL,
  discount DECIMAL(5, 2) DEFAULT 0,
  added_date DATETIMEOFFSET DEFAULT GETDATE(),
  CONSTRAINT UQ_User_Product UNIQUE (user_id, product_id)
);




-- Sample Data for the Cart Table
INSERT INTO Cart (user_id, product_id, quantity)
VALUES 
(1, 3, 1),    
(2, 1, 2),     
(4, 5, 1);      


CREATE PROCEDURE GetCartDetails
    @UserID INT
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Users WHERE ID = @UserID)
    BEGIN
        SELECT 'User not found.' AS Message;
        RETURN;
    END

    IF NOT EXISTS (SELECT 1 FROM Cart WHERE user_id = @UserID)
    BEGIN
        SELECT 'Cart is empty for this user.' AS Message;
        RETURN;
    END

    SELECT 
        U.full_name AS [Customer Name],
        P.product_name AS [Product Name],
        C.Quantity,
        C.Price AS [Unit Price],
        C.Discount,
        (C.Price - (C.Price * C.Discount / 100)) * C.Quantity AS [Total Per Item],
        C.added_date AS [Added Date Time],
        (SELECT SUM((C2.Price - (C2.Price * C2.Discount / 100)) * C2.Quantity) 
         FROM Cart C2 
         WHERE C2.user_id = @UserID) AS [Total Price]
    FROM Cart C
    JOIN users U ON C.user_id = U.ID
    JOIN products P ON C.product_id = P.ID
    WHERE C.user_id = @UserID
    ORDER BY C.added_date;
END;



-- Case 1: Retrieve Cart Details for admin_user (UserID = 1)
EXEC GetCartDetails @UserID = 1;


-- Case 2: Retrieve Cart Details for john_doe (UserID = 2)
EXEC GetCartDetails @UserID = 2;


-- Case 3: Try to Retrieve Cart for a Non-Existing User
EXEC GetCartDetails @UserID = 999;

select * from users
select * from products
select * from Cart





