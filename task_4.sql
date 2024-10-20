-- task_4.sql

-- Query the information_schema to get the full description of the 'books' table
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'  -- Specify the database
AND TABLE_NAME = 'books';              -- Specify the table name
