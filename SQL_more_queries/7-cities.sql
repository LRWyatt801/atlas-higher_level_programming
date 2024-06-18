-- Creates database "hbtn_0d_usa"
-- Creates table "cities" in database

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use database
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);