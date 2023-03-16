-- Creates the database hbtn_0d_usa and the table cities
CREATE DATABSE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY UNIQUE  NOT NULL AUTO-INCREMENT,
	state_id INT NOT NULL FOREIGN KEY(state_id),
	name VARCHAR(256) NOT NULL
);
