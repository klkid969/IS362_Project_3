CREATE SCHEMA IF NOT EXISTS project_3;
USE project_3;

CREATE TABLE population (
    column1 VARCHAR(255),
    column2 INT,
    column3 VARCHAR(255),
    -- Add more columns based on the CSV file structure
);
CREATE TABLE population (
    name VARCHAR(255),
    age INT,
    country VARCHAR(255)
);
CREATE TABLE population (
    name VARCHAR(255),
    age INT,
    country VARCHAR(255)
);
CREATE TABLE tb (
    country VARCHAR(255),
    year INT,
    gender VARCHAR(10),
    child INT,
    adult INT,
    elderly INT
);
ALTER TABLE tb
CHANGE COLUMN column1 country VARCHAR(255),
CHANGE COLUMN column2 year INT,
CHANGE COLUMN column3 sex VARCHAR(10),
CHANGE COLUMN column4 child INT,
CHANGE COLUMN column5 adult INT,
CHANGE COLUMN column6 elderly INT;
DESCRIBE tb;
SELECT 
    tb.country,
    tb.year,
    COALESCE(SUM(tb.child + tb.adult + tb.elderly), 0) / COALESCE(population.population, 1) AS rate
FROM 
    tb
JOIN 
    population ON tb.country = population.country AND tb.year = population.year
GROUP BY 
    tb.country, tb.year;
DESCRIBE population;

DESCRIBE tb;

SELECT tb.country, tb.year, IFNULL(SUM(tb.cases), 0) / IFNULL(p.population, 1) AS rate
FROM tb
JOIN population p ON tb.country = p.country AND tb.year = p.year
GROUP BY tb.country, tb.year;
DROP TABLE IF EXISTS population;
CREATE TABLE population (
    `Country:` VARCHAR(255),
    `Year:` INT,
    `Population:` INT
);
USE `DATABASE_Chinook`;
SHOW TABLES;
DROP DATABASE `DATABASE Chinook`;
CREATE DATABASE `DATABASE_Chinook`;
SELECT * FROM PlaylistTrack;

