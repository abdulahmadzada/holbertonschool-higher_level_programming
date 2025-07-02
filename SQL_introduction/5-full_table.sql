-- 4-show_table_description.sql
-- Script that prints the description of the table first_table from the current database
-- without using DESCRIBE or EXPLAIN statements

-- GET table description from information_schema
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_KEY, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';
