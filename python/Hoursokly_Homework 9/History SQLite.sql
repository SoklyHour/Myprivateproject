--- 23-11-2021 18:17:27
--- SQLite
DELETE FROM demo;

--- 23-11-2021 18:17:35
--- SQLite
DELETE FROM demo;

--- 23-11-2021 18:17:47
--- SQLite
-- TABLE
CREATE TABLE _class(
  id INT NOT null,
  name string, 
  code string,
  PRIMARY KEY (id)
  
  
  
);
CREATE TABLE _student(
  id INT NOT null,
  name string, 
  dob DATE,
  PRIMARY KEY (id)
  
  
  
);

-- INDEX
 
-- TRIGGER
 
-- VIEW;

--- 23-11-2021 18:17:52
--- SQLite
DELETE FROM demo;

--- 23-11-2021 18:17:59
--- SQLite
DROP TABLE demo;

--- 23-11-2021 18:22:59
--- SQLite
/***** ERROR ******
near "INSERT": syntax error
 ----- 
INSERT inTO _student(id, name, dob) VALUES (1, "ly", "13-09-2002")
INSERT inTO _student(id, name, dob) VALUES (2, "john", "13-09-2003")
INSERT inTO _student(id, name, dob) VALUES (3, "jack", "13-09-2004");
*****/

--- 23-11-2021 18:23:14
--- SQLite
/***** ERROR ******
near "INSERT": syntax error
 ----- 
INSERT inTO _student(id, name, dob) VALUES (1, "ly", "13-09-2002")
INSERT inTO _student(id, name, dob) VALUES (2, "john", "13-09-2003")
INSERT inTO _student(id, name, dob) VALUES (3, "jack", "13-09-2004");
*****/

--- 23-11-2021 18:23:17
--- SQLite
SELECT * FROM _student;

--- 23-11-2021 18:24:18
--- SQLite
INSERT INTO _student (id, name, dob) VALUES (1, "ly", "13-09-2002");

--- 23-11-2021 18:24:23
--- SQLite
SELECT * FROM _student;

--- 23-11-2021 18:25:44
--- SQLite
INSERT into _student (id, name, dob) VALUES (2,"John","13-09-2002");

--- 23-11-2021 18:26:04
--- SQLite
SELECT * FROM _student;

--- 23-11-2021 18:26:17
--- SQLite
UPDATE _student SET 
  id='2',
  name='John',
  dob='13-09-2003'
 WHERE id=2; SELECT * FROM _student;

--- 23-11-2021 18:26:32
--- SQLite
/***** ERROR ******
UNIQUE constraint failed: _student.id
 ----- 
INSERT into _student (id, name, dob) VALUES (2,"Jack","13-09-2004");
*****/

--- 23-11-2021 18:26:41
--- SQLite
INSERT into _student (id, name, dob) VALUES (3,"Jack","13-09-2004");

--- 23-11-2021 18:26:44
--- SQLite
SELECT * FROM _student;

--- 23-11-2021 18:30:57
--- SQLite
INSERT INTO _class (id, name , code) VALUES (1, "CSCI111", "CS111");

--- 23-11-2021 18:31:09
--- SQLite
/***** ERROR ******
UNIQUE constraint failed: _class.id
 ----- 
INSERT INTO _class (id, name , code) VALUES (1, "CSCI111", "CS111");
*****/

--- 23-11-2021 18:31:15
--- SQLite
SELECT * FROM _class;

--- 23-11-2021 18:31:44
--- SQLite
INSERT INTO _class (id, name , code) VALUES (2, "HIST101", "HIS101");

--- 23-11-2021 18:31:48
--- SQLite
SELECT * FROM _class;

--- 23-11-2021 18:32:19
--- SQLite
INSERT INTO _class (id, name , code) VALUES (3, "HUMN101", "HUM101");

--- 23-11-2021 18:32:21
--- SQLite
SELECT * FROM _class;

