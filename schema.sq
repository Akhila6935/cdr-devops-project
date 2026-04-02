CREATE DATABASE cdr_db;

USE cdr_db;

CREATE TABLE cdr_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    caller VARCHAR(15),
    receiver VARCHAR(15),
    duration INT,
    call_type VARCHAR(10),
    cost FLOAT,
    call_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
