-- Create table unique_id
-- id has default value 1 and must be unique
-- table creation should not fail if it exists

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
