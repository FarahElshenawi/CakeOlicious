USE Sweets_Store;
GO

DROP PROCEDURE IF EXISTS add_customer;
DROP PROCEDURE IF EXISTS AddNewProduct;
DROP PROCEDURE IF EXISTS AddProductDiscount;
DROP PROCEDURE IF EXISTS UpdateProductPrice;
DROP PROCEDURE IF EXISTS GetCartDetails;
DROP PROCEDURE IF EXISTS AddProductReview;
DROP PROCEDURE IF EXISTS GetProductReview;
DROP PROCEDURE IF EXISTS DeleteProductReview;
GO

-- Add Customer
CREATE PROCEDURE add_customer
    @username VARCHAR(100),
    @pass_word VARCHAR(255),
    @email VARCHAR(255),
    @full_name VARCHAR(100),
    @user_address TEXT = NULL,
    @phone_number VARCHAR(20) = NULL
AS
BEGIN
    IF EXISTS (SELECT 1 FROM users WHERE username = @username OR email = @email)
    BEGIN
        SELECT 'User already exists. Please try again with different user name or email.' AS Message;
    END
    ELSE
    BEGIN
        INSERT INTO users (username, pass_word, email, full_name, user_address, phone_number, user_role)
        VALUES (@username, @pass_word, @email, @full_name, @user_address, @phone_number, 'Customer');
        SELECT 'Customer added successfully!' AS Message;
    END
END;
GO

-- Add New Product
CREATE PROCEDURE AddNewProduct
    @product_name VARCHAR(100),
    @description TEXT = NULL,
    @price DECIMAL(10, 2),
    @stock INT,
    @category_id INT,
    @image_url VARCHAR(255) = NULL,
    @discount DECIMAL(5, 2) = 0
AS
BEGIN
    DECLARE @ExistingProductID INT;
    DECLARE @ExistingPrice DECIMAL(10, 2);
    IF NOT EXISTS (SELECT 1 FROM categories WHERE id = @category_id)
    BEGIN
        SELECT 'Invalid category_id. The category does not exist.' AS Message;
        RETURN;
    END
    SELECT @ExistingProductID = id, @ExistingPrice = price
    FROM products
    WHERE product_name = @product_name;
    IF @ExistingProductID IS NOT NULL
    BEGIN
        UPDATE products
        SET stock = stock + @stock
        WHERE id = @ExistingProductID;
        IF @ExistingPrice <> @price
        BEGIN
            UPDATE products
            SET price = @price
            WHERE id = @ExistingProductID;
            SELECT 'Product exists. Stock updated and price updated successfully!' AS Message;
        END
        ELSE
        BEGIN
            SELECT 'Product exists. Stock updated successfully!' AS Message;
        END
    END
    ELSE
    BEGIN
        INSERT INTO products (product_name, product_description, price, stock, category_id, image_url, discount)
        VALUES (@product_name, @description, @price, @stock, @category_id, @image_url, @discount);
        SELECT 'New product added successfully!' AS Message;
    END
END;
GO

-- Add Product Discount
CREATE PROCEDURE AddProductDiscount
    @product_name VARCHAR(100),
    @new_discount DECIMAL(5, 2)
AS
BEGIN
    DECLARE @ExistingProductID BIGINT;
    DECLARE @CurrentDiscount DECIMAL(5, 2);
    IF @new_discount < 0 OR @new_discount > 100
    BEGIN
        SELECT 'Invalid discount value. Please enter a value between 0 and 100.' AS Message;
        RETURN;
    END
    SELECT @ExistingProductID = id, @CurrentDiscount = discount
    FROM products
    WHERE product_name = @product_name;
    IF @ExistingProductID IS NOT NULL
    BEGIN
        IF @CurrentDiscount = @new_discount
        BEGIN
            SELECT 'The discount value is already the same. No changes made.' AS Message;
            RETURN;
        END
        UPDATE products
        SET discount = @new_discount
        WHERE id = @ExistingProductID;
        SELECT 'Discount applied successfully!' AS Message;
    END
    ELSE
    BEGIN
        SELECT 'Product not found.' AS Message;
    END
END;
GO

-- Update Product Price
CREATE PROCEDURE UpdateProductPrice
    @product_name VARCHAR(100),
    @new_price DECIMAL(10, 2)
AS
BEGIN
    DECLARE @ExistingProductID INT;
    DECLARE @CurrentPrice DECIMAL(10, 2);
    IF @new_price <= 0
    BEGIN
        SELECT 'Invalid price value. Please enter a positive value.' AS Message;
        RETURN;
    END
    SELECT @ExistingProductID = id, @CurrentPrice = price
    FROM products
    WHERE product_name = @product_name;
    IF @ExistingProductID IS NOT NULL
    BEGIN
        IF @CurrentPrice = @new_price
        BEGIN
            SELECT 'The price is already the same. No changes made.' AS Message;
            RETURN;
        END
        UPDATE products
        SET price = @new_price
        WHERE id = @ExistingProductID;
        SELECT 'Price updated successfully!' AS Message;
    END
    ELSE
    BEGIN
        SELECT 'Product not found.' AS Message;
    END
END;
GO

-- Get Cart Details
CREATE PROCEDURE GetCartDetails
    @UserID INT
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM users WHERE id = @UserID)
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
        u.full_name AS [Customer Name],
        p.product_name AS [Product Name],
        c.quantity,
        c.price AS [Unit Price],
        c.discount,
        (c.price - (c.price * c.discount / 100)) * c.quantity AS [Total Per Item],
        c.added_date AS [Added Date Time],
        (SELECT SUM((c2.price - (c2.price * c2.discount / 100)) * c2.quantity) 
         FROM Cart c2 
         WHERE c2.user_id = @UserID) AS [Total Price]
    FROM Cart c
    JOIN users u ON c.user_id = u.id
    JOIN products p ON c.product_id = p.id
    WHERE c.user_id = @UserID
    ORDER BY c.added_date;
END;
GO

-- Add Product Review
CREATE PROCEDURE AddProductReview
    @ProductName VARCHAR(100),
    @Username VARCHAR(100),
    @Rating INT,
    @ReviewText VARCHAR(MAX) = NULL
AS
BEGIN
    DECLARE @ProductID INT;
    DECLARE @UserID INT;
    DECLARE @ExistingReviewID INT;
    DECLARE @ExistingReviewText VARCHAR(MAX);
    IF @Rating < 1 OR @Rating > 5
    BEGIN
        SELECT 'Invalid rating. Rating must be between 1 and 5.' AS Message;
        RETURN;
    END
    SELECT @ProductID = id
    FROM products
    WHERE product_name = @ProductName;
    IF @ProductID IS NULL
    BEGIN
        SELECT 'Product not found.' AS Message;
        RETURN;
    END
    SELECT @UserID = id
    FROM users
    WHERE username = @Username;
    IF @UserID IS NULL
    BEGIN
        SELECT 'User not found.' AS Message;
        RETURN;
    END
    SELECT @ExistingReviewID = id, @ExistingReviewText = review_text
    FROM product_reviews
    WHERE product_id = @ProductID AND user_id = @UserID;
    IF @ExistingReviewID IS NOT NULL
    BEGIN
        IF @ExistingReviewText = @ReviewText
        BEGIN
            SELECT 'Error: Duplicate review. Your review is identical to the previous one.' AS Message;
            RETURN;
        END
    END
    INSERT INTO product_reviews (product_id, user_id, rating, review_text)
    VALUES (@ProductID, @UserID, @Rating, @ReviewText);
    SELECT 'Review successfully added.' AS Message;
END;
GO

-- Get Product Review
CREATE PROCEDURE GetProductReview
    @ProductName VARCHAR(100),
    @Username VARCHAR(100)
AS
BEGIN
    IF LTRIM(RTRIM(@ProductName)) = '' OR LTRIM(RTRIM(@Username)) = ''
    BEGIN
        SELECT 'Error: Product name and username cannot be empty.' AS Message;
        RETURN;
    END
    DECLARE @ProductID INT;
    DECLARE @UserID INT;
    SELECT @ProductID = id
    FROM products
    WHERE product_name = @ProductName;
    IF @ProductID IS NULL
    BEGIN
        SELECT 'Product not found.' AS Message;
        RETURN;
    END
    SELECT @UserID = id
    FROM users
    WHERE username = @Username;
    IF @UserID IS NULL
    BEGIN
        SELECT 'User not found.' AS Message;
        RETURN;
    END
    IF NOT EXISTS (
        SELECT 1
        FROM product_reviews PR
        WHERE PR.product_id = @ProductID AND PR.user_id = @UserID
    )
    BEGIN
        SELECT 'No review found for this product by this user.' AS Message;
    END
    ELSE
    BEGIN
        SELECT 
            u.full_name AS Username,
            p.product_name AS ProductName,
            PR.rating AS Rating,
            PR.review_text AS ReviewText,
            PR.review_date AS ReviewDate
        FROM product_reviews PR
        JOIN users u ON PR.user_id = u.id
        JOIN products p ON PR.product_id = p.id
        WHERE PR.product_id = @ProductID AND PR.user_id = @UserID;
    END
END;
GO

-- Delete Product Review
CREATE PROCEDURE DeleteProductReview
    @ProductName VARCHAR(100),
    @Username VARCHAR(100)
AS
BEGIN
    DECLARE @ProductID INT;
    DECLARE @UserID INT;
    DECLARE @ReviewID INT;
    BEGIN TRANSACTION;
    BEGIN TRY
        SELECT @ProductID = id
        FROM products
        WHERE product_name = @ProductName;
        SELECT @UserID = id
        FROM users
        WHERE username = @Username;
        IF @ProductID IS NULL OR @UserID IS NULL
        BEGIN
            ROLLBACK TRANSACTION;
            SELECT 'Product or User not found.' AS Message;
            RETURN;
        END
        SELECT @ReviewID = id
        FROM product_reviews
        WHERE product_id = @ProductID AND user_id = @UserID;
        IF @ReviewID IS NULL
        BEGIN
            ROLLBACK TRANSACTION;
            SELECT 'No review found for this product by this user.' AS Message;
            RETURN;
        END
        DELETE FROM product_reviews
        WHERE id = @ReviewID;
        IF @@ROWCOUNT > 0
        BEGIN
            COMMIT TRANSACTION;
            SELECT 'Review successfully deleted.' AS Message;
        END
        ELSE
        BEGIN
            ROLLBACK TRANSACTION;
            SELECT 'Error: Review deletion failed.' AS Message;
        END
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        SELECT ERROR_MESSAGE() AS ErrorMessage;
    END CATCH
END;
GO
