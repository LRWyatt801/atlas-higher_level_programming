-- Creates a database "hbtn_0d_usa"
-- Creates table in database called "states"

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use database
USE hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);