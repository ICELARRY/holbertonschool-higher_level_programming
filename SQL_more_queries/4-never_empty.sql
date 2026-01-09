-- Create table id_not_null
-- id has default value 1, table creation should not fail if it exists

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
