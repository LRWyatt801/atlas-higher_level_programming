-- Creates a database and user

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create User
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant select permission
GRANT SELECT ON 'hbtn_0d_2'.* TO 'hbtn_0d_2'@'localhost';