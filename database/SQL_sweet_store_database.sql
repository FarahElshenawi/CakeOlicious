use Sweets_Store;

-- create users table
--############################################
CREATE TABLE users (
    id INT PRIMARY KEY IDENTITY(1,1),
    username VARCHAR(100) UNIQUE NOT NULL,
    pass_word VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    user_address TEXT,
    phone_number VARCHAR(20),
    user_role VARCHAR(20) CHECK (user_role IN ('Admin', 'Customer')) NOT NULL
);

-- add samples for users
INSERT INTO users (username, pass_word, email, full_name, user_address, phone_number, user_role)
VALUES 
('admin_user', 'Admin1234!', 'admin@sweetsstore.com', 'Admin User', '123 Admin Street, Candy City', '123-456-7890', 'Admin'),
('john_doe', 'Password123!', 'john.doe@email.com', 'John Doe', '456 Sweet Lane, Sugar Town', '987-654-3210', 'Customer'),
('jane_smith', 'JanePass2025!', 'jane.smith@email.com', 'Jane Smith', '789 Chocolate Ave, Choco City', '555-123-4567', 'Customer'),
('mike_brown', 'MikeBrown2025!', 'mike.brown@email.com', 'Mike Brown', '101 Candy Blvd, Candy City', '222-333-4444', 'Customer');

-- create categories table
--##########################################
CREATE TABLE categories (
    id INT PRIMARY KEY IDENTITY(1,1),
    category_name VARCHAR(50) NOT NULL,
    category_description TEXT
);


INSERT INTO categories (category_name, category_description)
VALUES 
('Chocolate', 'All kinds of delicious chocolates including milk, dark, and white chocolate.'),
('Candy', 'Various candies from gummies to hard candies, perfect for a sweet treat.'),
('Bakery', 'Freshly baked goods including cakes, cookies, and pastries.'),
('Ice Cream', 'Creamy and delicious ice cream in various flavors and styles.');


-- create products table
--###########################################
CREATE TABLE products (
    id INT PRIMARY KEY IDENTITY(1,1),
    product_name VARCHAR(100) NOT NULL,
    product_description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    category_id INT NOT NULL,
    image_url VARCHAR(255),
    discount DECIMAL(5, 2) DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- create product_reviews table
--#####################################################
CREATE TABLE product_reviews (
    id INT PRIMARY KEY IDENTITY(1,1),
    product_id INT,
    user_id INT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    review_text TEXT,
    review_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


INSERT INTO products (product_name, product_description, price, stock, category_id, image_url, discount)
VALUES 
('Milk Chocolate Bar', 'Delicious creamy milk chocolate.', 5.99, 100, 1, 'https://example.com/images/milk_chocolate.jpg', 0),
('Gummy Bears', 'Colorful gummy bears with fruity flavors.', 2.99, 200, 2, 'https://example.com/images/gummy_bears.jpg', 10.00),
('Chocolate Cake', 'Rich chocolate cake with creamy frosting.', 15.50, 50, 3, 'https://example.com/images/chocolate_cake.jpg', 5.00),
('Vanilla Ice Cream', 'Smooth vanilla ice cream.', 4.99, 80, 4, 'https://example.com/images/vanilla_ice_cream.jpg', 0),
('Dark Chocolate Bar', 'High-quality dark chocolate.', 6.99, 120, 1, 'https://example.com/images/dark_chocolate.jpg', 0),
('Candy Cane', 'Sweet peppermint candy stick.', 1.50, 300, 2, 'https://example.com/images/candy_cane.jpg', 20.00);

-- create orders table
CREATE TABLE orders (
    id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('Pending', 'Shipped', 'Delivered')) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


INSERT INTO orders (user_id, total_amount, status)
VALUES 
(2, 29.99, 'Pending'),       -- New request for customer with ID 2
(3, 45.50, 'Shipped'),       -- New request for customer with ID 3
(4, 15.99, 'Delivered'),     -- New request for customer with ID 4
(2, 8.75, 'Pending'),        -- New request for customer with ID 2
(3, 60.00, 'Shipped');       -- New request for customer with ID 3


-- create order_details table and added sampels

CREATE TABLE order_details (
    id INT PRIMARY KEY IDENTITY(1,1),
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO order_details (order_id, product_id, quantity, price)
VALUES 
(1, 1, 2, 5.99),     -- Order 1 contains 2 pieces of "Milk Chocolate Bar" priced at 5.99 each.
(1, 2, 1, 2.99),     -- Order 1 contains 1 piece of "Gummy Bears" priced at 2.99.
(2, 3, 1, 15.50),    -- Order 2 contains 1 piece of "Chocolate Cake" priced at 15.50.
(3, 5, 2, 6.99),     -- Order 3 contains 2 pieces of "Dark Chocolate Bar" priced at 6.99 each.
(4, 6, 3, 1.50),     -- Order 4 contains 3 pieces of "Candy Cane" priced at 1.50 each.
(5, 4, 4, 4.99);     -- Order 5 contains 4 pieces of "Vanilla Ice Cream" priced at 4.99 each.


-- create payments table and added sampels
CREATE TABLE payments (
    id INT PRIMARY KEY IDENTITY(1,1),
    order_id INT,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(20) CHECK (payment_method IN ('Credit Card', 'PayPal', 'Bank Transfer', 
	'Cash on Delivery', 'Gift Card')) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('Pending', 'Completed')) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);


INSERT INTO payments (order_id, amount, payment_method, status)
VALUES 
(1, 29.99, 'Credit Card', 'Completed'),          -- Payment for Order 1 via Credit Card
(2, 45.50, 'PayPal', 'Completed'),               -- Payment for Order 2 via PayPal
(3, 15.99, 'Bank Transfer', 'Completed'),        -- Payment for Order 3 via Bank Transfer
(4, 8.75, 'Cash on Delivery', 'Pending'),        -- Payment for Order 4 via Cash on Delivery
(5, 60.00, 'Gift Card', 'Completed');            -- Payment for Order 5 via Gift Card


--################################################# PROCEDURES ################################################################
--#############################################################################################################################


--################################################# add customer###############################################################
--##########################################################################################################################

CREATE PROCEDURE add_customer
    @username VARCHAR(100),
    @pass_word VARCHAR(255),
    @email VARCHAR(255),
    @full_name VARCHAR(100),
    @user_address TEXT = NULL,
    @phone_number VARCHAR(20) = NULL
AS
BEGIN
    -- Check if the customer already exists
    IF EXISTS (SELECT 1 FROM users WHERE username = @username OR email = @email)
    BEGIN
        SELECT 'User already exists. Please try again with different user name or email.' AS Message;
    END
    ELSE
    BEGIN
        -- Insert the new customer
        INSERT INTO users (username, pass_word, email, full_name, user_address, phone_number, user_role)
        VALUES (@username, @pass_word, @email, @full_name, @user_address, @phone_number, 'Customer');
        
        SELECT 'Customer added successfully!' AS Message;
    END
END;


--################################################# add product#################################################################
--#################################################################################################################################

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

    -- Check if the category_id exists in the categories table
    IF NOT EXISTS (SELECT 1 FROM categories WHERE id = @category_id)
    BEGIN
        SELECT 'Invalid category_id. The category does not exist.' AS Message;
        RETURN;
    END

    -- Check if the product already exists by name
    SELECT @ExistingProductID = id, @ExistingPrice = price
    FROM products
    WHERE product_name = @product_name;

    IF @ExistingProductID IS NOT NULL
    BEGIN
        -- Update the stock
        UPDATE products
        SET stock = stock + @stock
        WHERE id = @ExistingProductID;

        -- Update the price if it's different
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
        -- Insert the new product
        INSERT INTO products (product_name, product_description, price, stock, category_id, image_url, discount)
        VALUES (@product_name, @description, @price, @stock, @category_id, @image_url, @discount);

        SELECT 'New product added successfully!' AS Message;
    END
END;

-- for check the AddNewProduct
EXEC AddNewProduct 
    @product_name = 'Milk Chocolate Bar',
    @description = 'Creamy and delicious milk chocolate bar.',
    @price = 6.50,
    @stock = 150,
    @category_id = 1,   -- The category is in the table 
    @image_url = 'https://example.com/milk_chocolate.jpg',
    @discount = 0;


EXEC AddNewProduct 
    @product_name = 'Strawberry Cake',
    @description = 'Delicious strawberry cake with creamy frosting.',
    @price = 12.00,
    @stock = 30,
    @category_id = 999,  -- the category not found
    @image_url = 'https://example.com/strawberry_cake.jpg',
    @discount = 0;



EXEC AddNewProduct 
    @product_name = 'white Chocolate',
    @description = 'Creamy and delicious milk chocolate bar.',
    @price = 6.50,
    @stock = 150,
    @category_id = 1,   -- The category is in the table 
    @image_url = 'https://example.com/milk_chocolate.jpg',
    @discount = 0;


--################################################# add discount for any product###############################################
--#############################################################################################################################


CREATE PROCEDURE AddProductDiscount
    @product_name VARCHAR(100),

    @new_discount DECIMAL(5, 2)
AS
BEGIN
    DECLARE @ExistingProductID BIGINT;
    DECLARE @CurrentDiscount DECIMAL(5, 2);

    -- Validate the discount value
    IF @new_discount < 0 OR @new_discount > 100
    BEGIN
        SELECT 'Invalid discount value. Please enter a value between 0 and 100.' AS Message;
        RETURN;
    END

    -- Check if the product exists
    SELECT @ExistingProductID = id, @CurrentDiscount = discount
    FROM products
    WHERE product_name = @product_name;

    IF @ExistingProductID IS NOT NULL
    BEGIN
        -- Check if the new discount is the same as the current discount
        IF @CurrentDiscount = @new_discount
        BEGIN
            SELECT 'The discount value is already the same. No changes made.' AS Message;
            RETURN;
        END

        -- Update the product's discount
        UPDATE products
        SET discount = @new_discount
        WHERE id = @ExistingProductID;

        SELECT 'Discount applied successfully!' AS Message;
    END
    ELSE
    BEGIN
        -- Product not found
        SELECT 'Product not found.' AS Message;
    END
END;

--Scenario 1: Valid Discount for an Existing Product (Updating Discount).
EXEC AddProductDiscount 
    @product_name = 'Milk Chocolate Bar',
    @new_discount = 15.00;

-- Scenario 2: Same Discount as Current One.
EXEC AddProductDiscount 
    @product_name = 'Milk Chocolate Bar',
    @new_discount = 15.00;

--Scenario 3: Invalid Discount Value (Less than 0% or Greater than 100%).
EXEC AddProductDiscount 
    @product_name = 'Milk Chocolate Bar',
    @new_discount = -5.00;

EXEC AddProductDiscount 
    @product_name = 'Milk Chocolate Bar',
    @new_discount = 120.00;

--Scenario 4: Product Not Found in the Database.
EXEC AddProductDiscount 
    @product_name = 'Banana Cake', 
    @new_discount = 10.00;


--################################################# update product price###################################################
--##########################################################################################################################

CREATE PROCEDURE UpdateProductPrice
    @product_name VARCHAR(100),
    @new_price DECIMAL(10, 2)
AS
BEGIN
    DECLARE @ExistingProductID INT;
    DECLARE @CurrentPrice DECIMAL(10, 2);

    -- Validate the price value
    IF @new_price <= 0
    BEGIN
        SELECT 'Invalid price value. Please enter a positive value.' AS Message;
        RETURN;
    END

    -- Check if the product exists
    SELECT @ExistingProductID = id, @CurrentPrice = price
    FROM products
    WHERE product_name = @product_name;

    IF @ExistingProductID IS NOT NULL
    BEGIN
        -- Check if the new price is the same as the current price
        IF @CurrentPrice = @new_price
        BEGIN
            SELECT 'The price is already the same. No changes made.' AS Message;
            RETURN;
        END

        -- Update the product's price
        UPDATE products
        SET price = @new_price
        WHERE id = @ExistingProductID;

        SELECT 'Price updated successfully!' AS Message;
    END
    ELSE
    BEGIN
        -- Product not found
        SELECT 'Product not found.' AS Message;
    END
END;


-- Scenario 1: Valid Price Update for an Existing Product.
EXEC UpdateProductPrice 
    @product_name = 'Milk Chocolate Bar',
    @new_price = 8.50;
-- Scenario 2: Same Price as Current One.

EXEC UpdateProductPrice 
    @product_name = 'Milk Chocolate Bar',
    @new_price = 8.50;

-- Scenario 3: Invalid Price Value (Zero or Negative).
EXEC UpdateProductPrice 
    @product_name = 'Milk Chocolate Bar',
    @new_price = -1.00;

EXEC UpdateProductPrice 
    @product_name = 'Milk Chocolate Bar',
    @new_price = 0.00;

-- Scenario 4: Product Not Found.
EXEC UpdateProductPrice 
    @product_name = 'Banana Cake', 
    @new_price = 12.00;


--################################################# delete product##########################################################
--############################################################################################################################

CREATE PROCEDURE DeleteProduct
    @product_name VARCHAR(100),
    @ConfirmDeletion VARCHAR(10)
AS
BEGIN
    DECLARE @ExistingProductID INT;
    DECLARE @OrderID INT;
    DECLARE @OrderStatus VARCHAR(20);
    DECLARE @OrderCount INT;

    IF @ConfirmDeletion <> 'Yes'
    BEGIN
        SELECT 'Deletion cancelled. Please confirm deletion by passing Confirm Deletion = ''Yes''.' AS Message;
        RETURN;
    END

    -- Check if the product exists
    SELECT @ExistingProductID = id
    FROM products
    WHERE product_name = @product_name;

    IF @ExistingProductID IS NOT NULL
    BEGIN
        -- Check if the product is linked to orders
        SELECT @OrderCount = COUNT(*)
        FROM order_details
        WHERE product_id = @ExistingProductID;

        IF @OrderCount > 0
        BEGIN
            -- Retrieve the Order ID & Status for this product
            SELECT TOP 1 @OrderID = order_id, @OrderStatus = O.status
            FROM order_details OD
            JOIN orders O ON OD.order_id = O.id
            WHERE OD.product_id = @ExistingProductID;

            IF @OrderStatus = 'Delivered'
            BEGIN
                -- Delete related order_details
                DELETE FROM order_details
                WHERE product_id = @ExistingProductID;

                -- Delete the related order
                DELETE FROM orders
                WHERE id = @OrderID;

                -- Delete the product
                DELETE FROM products
                WHERE id = @ExistingProductID;

                SELECT 'Product deleted successfully! It was linked to a delivered order, which has also been deleted.' AS Message;
            END
            ELSE
            BEGIN
                SELECT 'Product cannot be deleted because it is linked to an active order (Status: ' + @OrderStatus + ').' AS Message;
            END
        END
        ELSE
        BEGIN
            -- Delete the product
            DELETE FROM products
            WHERE id = @ExistingProductID;

            SELECT 'Product deleted successfully!' AS Message;
        END
    END
    ELSE
    BEGIN
        -- Product not found
        SELECT 'Product not found.' AS Message;
    END
END;



-- Scenario 1: Product Linked to Active Order (Pending or Shipped)
EXEC DeleteProduct @product_name = 'Candy Cane', @ConfirmDeletion = 'Yes';


-- Scenario 2: Product Not Found
EXEC DeleteProduct @product_name = 'Non-Existent Product', @ConfirmDeletion = 'Yes';


--################################################# search product###################################################
--######################################################################################################################

CREATE PROCEDURE SearchProduct
    @ProductName VARCHAR(100) = NULL,
    @CategoryName VARCHAR(100) = NULL,
    @MinPrice DECIMAL(10, 2) = NULL,
    @MaxPrice DECIMAL(10, 2) = NULL,
    @MinDiscount DECIMAL(5, 2) = 0,        -- Minimum discount allowed
    @OnlyDiscounted BIT = 0,                -- If set to 1, only fetch products with discount > 0
    @SortBy VARCHAR(20) = 'price',          -- Options: 'price', 'product_name', 'discount'
    @SortOrder VARCHAR(4) = 'ASC',          -- Options: 'ASC', 'DESC'
    @RowLimit INT = 100                     -- Limit the number of returned rows
AS
BEGIN
    -- Validate SortBy and SortOrder
    DECLARE @SafeSortBy NVARCHAR(20) = CASE @SortBy
        WHEN 'price' THEN 'P.price'
        WHEN 'product_name' THEN 'P.product_name'
        WHEN 'discount' THEN 'P.discount'
        ELSE 'P.price'
    END;
    DECLARE @SafeSortOrder NVARCHAR(4) = CASE @SortOrder
        WHEN 'ASC' THEN 'ASC'
        WHEN 'DESC' THEN 'DESC'
        ELSE 'ASC'
    END;

    DECLARE @Query NVARCHAR(MAX);

    SET @Query = N'
    SELECT TOP (' + CAST(@RowLimit AS NVARCHAR) + ')
        P.product_name,
        P.product_description,
        P.price,
        P.stock,
        P.discount,
        P.image_url,
        C.category_name
    FROM products P
    JOIN categories C ON P.category_id = C.id
    WHERE 
        (@ProductName IS NULL OR P.product_name LIKE ''%'' + @ProductName + ''%'')
        AND (@CategoryName IS NULL OR C.category_name = @CategoryName)
        AND (@MinPrice IS NULL OR P.price >= @MinPrice)
        AND (@MaxPrice IS NULL OR P.price <= @MaxPrice)
        AND (P.discount >= @MinDiscount) ';

    -- Add filter for discounted products if required
    IF @OnlyDiscounted = 1
    BEGIN
        SET @Query += ' AND P.discount > 0 ';
    END;

    -- Add sorting condition
    SET @Query += ' ORDER BY ' + @SafeSortBy + ' ' + @SafeSortOrder + ';';
    
    EXEC sp_executesql @Query,
        N'@ProductName VARCHAR(100), @CategoryName VARCHAR(100), @MinPrice DECIMAL(10, 2), 
          @MaxPrice DECIMAL(10, 2), @MinDiscount DECIMAL(5, 2)',
        @ProductName, @CategoryName, @MinPrice, @MaxPrice, @MinDiscount;
END;


-- Find products with a discount only sorted by discount in descending order

EXEC SearchProduct 
    @OnlyDiscounted = 1,
    @SortBy = 'discount',
    @SortOrder = 'DESC';


-- Find products between the price of 5 and 20, sorted by name in ascending order
EXEC SearchProduct 
    @MinPrice = 5,
    @MaxPrice = 20,
    @SortBy = 'product_name',
    @SortOrder = 'ASC';

--################################################# update product stock####################################################
--##############################################################################################################################
CREATE PROCEDURE UpdateProductStock
    @ProductName VARCHAR(100),
    @NewStock INT,
    @AddToExisting BIT = 1  --1: Add to existing inventory, 0: Replace existing inventory.
AS
BEGIN
    DECLARE @ExistingProductID BIGINT;
    DECLARE @CurrentStock INT;

    -- Check that the new quantity is positive
    IF @NewStock <= 0
    BEGIN
        SELECT 'Invalid stock value. New stock must be greater than zero.' AS Message;
        RETURN;
    END

    -- Check the presence of the product in the database
    SELECT @ExistingProductID = id, @CurrentStock = stock
    FROM products
    WHERE product_name = @ProductName;

    IF @ExistingProductID IS NULL
    BEGIN
        SELECT 'Product not found.' AS Message;
        RETURN;
    END

    -- Update inventory based on selected addition method
    IF @AddToExisting = 1
    BEGIN
        UPDATE products
        SET stock = stock + @NewStock
        WHERE id = @ExistingProductID;
        
        SELECT 'Product stock successfully updated by adding the new quantity.' AS Message;
    END
    ELSE
    BEGIN
        UPDATE products
        SET stock = @NewStock
        WHERE id = @ExistingProductID;
        
        SELECT 'Product stock successfully updated by replacing the old quantity.' AS Message;
    END
END;


-- Added 30 new pieces for a product named "Candy Bar"
EXEC UpdateProductStock 'Milk Chocolate Bar', 30, 1;


--Replace existing stock with a new value of 100 pieces
EXEC UpdateProductStock 'Milk Chocolate Bar' , 100, 0;

-- Trying to enter a negative quantity
EXEC UpdateProductStock 'Milk Chocolate Bar', -10, 1;


--################################################# add product review###################################################
--#####################################################################################################################

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

    -- Verify that the rating is between 1 and 5
    IF @Rating < 1 OR @Rating > 5
    BEGIN
        SELECT 'Invalid rating. Rating must be between 1 and 5.' AS Message;
        RETURN;
    END

    -- Get the product ID
    SELECT @ProductID = id
    FROM products
    WHERE product_name = @ProductName;

    IF @ProductID IS NULL
    BEGIN
        SELECT 'Product not found.' AS Message;
        RETURN;
    END

    -- Get user ID
    SELECT @UserID = id
    FROM users
    WHERE username = @Username;

    IF @UserID IS NULL
    BEGIN
        SELECT 'User not found.' AS Message;
        RETURN;
    END

    -- Check for a previous review
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

    -- Enter the new revision in the table
    INSERT INTO product_reviews (product_id, user_id, rating, review_text)
    VALUES (@ProductID, @UserID, @Rating, @ReviewText);

    SELECT 'Review successfully added.' AS Message;
END;

--1: Add a new rating correctly
EXEC AddProductReview
    @ProductName = 'Milk Chocolate Bar',
    @Username = 'john_doe',
    @Rating = 5,
    @ReviewText = 'Amazing chocolate! Highly recommend.';


--################################################# get product review####################################################
--########################################################################################################################


CREATE PROCEDURE GetProductReview
    @ProductName VARCHAR(100),
    @Username VARCHAR(100)
AS
BEGIN
    -- Check if inputs are empty
    IF LTRIM(RTRIM(@ProductName)) = '' OR LTRIM(RTRIM(@Username)) = ''
    BEGIN
        SELECT 'Error: Product name and username cannot be empty.' AS Message;
        RETURN;
    END

    DECLARE @ProductID INT;
    DECLARE @UserID INT;

    -- Check for product and user existence
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

    -- Check if the review exists
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
            U.full_name AS Username,
            P.product_name AS ProductName,
            PR.rating AS Rating,
            PR.review_text AS ReviewText,
            PR.review_date AS ReviewDate
        FROM product_reviews PR
        JOIN users U ON PR.user_id = U.id
        JOIN products P ON PR.product_id = P.id
        WHERE PR.product_id = @ProductID AND PR.user_id = @UserID;
    END
END;

-- Test Case 1: Product and User both exist, and the user has reviewed the product
EXEC GetProductReview @ProductName = 'Milk Chocolate Bar', @Username = 'john_doe';

-- Test Case 2: Product doesn't exist
EXEC GetProductReview @ProductName = 'NonExistingProduct', @Username = 'john_doe';

-- Test Case 3: User doesn't exist
EXEC GetProductReview @ProductName = 'Milk Chocolate Bar', @Username = 'NonExistingUser';

-- Test Case 4: Valid product and user, but review doesn't exist
EXEC GetProductReview @ProductName = 'Milk Chocolate Bar', @Username = 'jane_smith';


--################################################# delete product review########################################################
--############################################################################################################################
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
        -- Retrieve ProductID
        SELECT @ProductID = id
        FROM products
        WHERE product_name = @ProductName;

        -- Retrieve UserID
        SELECT @UserID = id
        FROM users
        WHERE username = @Username;

        -- Check if the product and user exist
        IF @ProductID IS NULL OR @UserID IS NULL
        BEGIN
            ROLLBACK TRANSACTION;
            SELECT 'Product or User not found.' AS Message;
            RETURN;
        END

        -- Retrieve the review ID
        SELECT @ReviewID = id
        FROM product_reviews
        WHERE product_id = @ProductID AND user_id = @UserID;

        -- Check if the review exists
        IF @ReviewID IS NULL
        BEGIN
            ROLLBACK TRANSACTION;
            SELECT 'No review found for this product by this user.' AS Message;
            RETURN;
        END

        -- Delete the review from the product_reviews table
        DELETE FROM product_reviews
        WHERE id = @ReviewID;

        -- Check if the deletion was successful
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
        -- Rollback transaction in case of an error
        ROLLBACK TRANSACTION;
        SELECT ERROR_MESSAGE() AS ErrorMessage;
    END CATCH
END;


-- test : Call the DeleteProductReview procedure
EXEC DeleteProductReview @ProductName = 'Milk Chocolate Bar', @Username = 'jane_smith';


select * from product_reviews 
select * from products
select * from users