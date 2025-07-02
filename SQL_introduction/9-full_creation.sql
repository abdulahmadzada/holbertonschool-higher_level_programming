-- 8-second_table.sql
-- Script that creates table second_table and inserts multiple rows
-- The table is created only if it does not exist

CREATE TABLE IF NOT EXISTS second_table (
    id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8)
