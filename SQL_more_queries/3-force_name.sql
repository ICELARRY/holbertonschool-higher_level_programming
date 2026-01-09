-- Create table force_name with id and name columns
-- name cannot be NULL, table creation should not fail if it exists

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
