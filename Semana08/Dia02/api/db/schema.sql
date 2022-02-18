CREATE DATABASE IF NOT EXISTS company;
USE company;
CREATE TABLE employee(
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) DEFAULT NULL,
    salary INT(11) DEFAULT NULL,
    PRIMARY KEY (id)
);

INSERT INTO employee(name,salary) VALUES
    ('José',1000),
    ('Maria',2000),
    ('João',3000),
    ('Pedro',4000),
    ('Ana',5000),
    ('Paulo',6000),
    ('Julia',7000),
    ('Rafael',8000),
    ('Carla',9000);
    
