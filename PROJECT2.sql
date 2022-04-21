
---------------Distributer_details------------------------

CREATE TABLE Distributer_details(
Distributer_id INT NOT NULL PRIMARY KEY IDENTITY(1000,1),
First_name varchar(50) not null,
Middle_Name varchar(50) not null,
Last_name varchar(50) not null,
Area varchar(50) not null,
City varchar(50) not null)



insert into Distributer_details values
('Harish','Rajesh','Kanoje','Kharbi','Nagpur'),
('Kajal','Chandrakant','Palkhade','Pratap Nagar','Nagpur'),
('Hrishikesh','Bhimrao','Dhone','Shubhash Nagar','Nagpur'),
('Kunal','Hrishi','Nandeshwar','Indora','Nagpur');


----------------------------Distributer_login--------------------------------------

CREATE TABLE Distributer_login(
Distributer_id int not null ,
Password varchar(50) not null, 
CONSTRAINT Distributer_id FOREIGN KEY (Distributer_id)
REFERENCES Distributer_details(Distributer_id))

INSERT INTO Distributer_login (Distributer_id,Password)
values(1000,'ABC@4567'),
(1001,'DEF@8415'),
(1002,'QWE@786'),
(1003,'SAE@4201');

-------------------------Customer_Details_Table-----------------------------

create table Customer_Details_Table(
Ration_no int not null primary key IDENTITY(200000,1),
Area varchar(50),
City varchar(50),
Category varchar(10) check(Category in ('SC','OBC','ST','OPEN')),
Family_Income money,
Card_type varchar(10) check(Card_type in ('Yellow','Saffron','White')),
Distributer_Id int foreign key references Distributer_details(Distributer_Id)
)

INSERT INTO Customer_Details_Table(
Area,
City,
Category,
Family_Income,
Card_type,
Distributer_ID
)
VALUES
('Kharbi', 'Nagpur', 'OBC', 90000, 'Saffron', 1000),
('Kharbi', 'Nagpur', 'SC', 25000, 'Yellow', 1000),
('Kharbi', 'Nagpur', 'ST', 120000, 'White', 1000),
('Pratap Nagar', 'Nagpur', 'OPEN', 20000, 'Yellow', 1001),
('Pratap Nagar', 'Nagpur', 'OBC', 50000, 'Saffron', 1001),
('Pratap Nagar', 'Nagpur', 'ST', 70000, 'Saffron', 1001),
('Pratap Nagar', 'Nagpur', 'OPEN', 130000, 'White', 1001),
('Shubhash Nagar', 'Nagpur', 'ST', 12000, 'Yellow', 1002),
('Shubhash Nagar', 'Nagpur', 'OBC', 190000, 'White', 1002),
('Shubhash Nagar', 'Nagpur', 'OPEN', 10000, 'Yellow', 1002),
('Shubhash Nagar', 'Nagpur', 'ST', 50000, 'Saffron', 1002),
('Indora', 'Nagpur', 'OPEN', 35000, 'Saffron', 1003),
('Indora', 'Nagpur', 'OBC', 70000, 'Saffron', 1003),
('Indora', 'Nagpur', 'SC', 15000, 'Yellow', 1003),
('Indora', 'Nagpur', 'OPEN', 200000, 'White', 1003)

-------------------Customer_family_details------------------------------

CREATE TABLE Customer_family_details(
Ration_no int  foreign key references Customer_Details_Table(Ration_no),
First_Name varchar(50),
Middle_Name varchar(50),
Last_Name Varchar(50),
Age int)


INSERT INTO Customer_family_details(Ration_no, First_Name, Middle_Name, Last_Name, Age)
VALUES
(200000, 'Surender', 'Rakesh', 'Singh', 30),
(200000, 'Sanni', 'Surender', 'Singh', 15),
(200000,'Rashmi','Surender','singh',8),
(200000,'vanshika','Surender','sing',28),
(200001,'Soham','Jagdish','Rana',56),
(200001,'Swati','Soham','Rana',50),
(200002,'Sarang','Mhonanrao','Sharma',37),
(200002,'vivek','Sarang','Sharma',10),
(200002,'Arti','Sarang','Sharma',33),
(200003,'Kisanrao','Ramrao','Wanve',44),
(200003,'Sonu','Kisanrao','Wanve',20),
(200003,'Monu','Kisanrao','Wanve',18),
(200004,'Suresh','Kumar','Yadav',80),
(200004,'Vikram','Kumar','Yadav',76),
(200004,'Rajani','Suresh','Yadav',70),
(200004,'Sushila','Suresh','Yadav',42),
(200004,'Raj','Suresh','Yadav',50),
(200005,'Dharaj','Shriram','Wankhade',75),
(200005,'Indu','Dharaj','Wankhade',70),
(200005,'Adhiraj','Dharaj','Wankhade',55),
(200005,'Ananta','Adhiraj','Wankhade',20),
(200006,'Ramesh','Manikrao','Raut',60),
(200006,'Alka','Ramesh','Raut',57),
(200006,'Rani','Ramesh','Raut',35),
(200007,'Sanjay','Nilu','Das',20),
(200008,'Santosh','Gopal','Mehta',33),
(200008,'Nikita','Santosh','Mehta',28),
(200009,'Santosh','Ramesh','Mahalle',40),
(200009,'Sushila','Santosh','Mahalle',36),
(200009,'Saurab','Santosh','Mahalle',14),
(200009,'Shivam','Santosh','Mahalle',16),
(200010,'Karishma','Balu','Dahake',50),
(200011,'Baburao','Pradiprao','Solanke',30),
(200012,'Usha','Baburao','Solanke',28),
(200012,'pinky','Baburao','Solanke',5),
(200013,'Samakhs','Vilash','Jadhav',60),
(200013,'Madhuri','Samakhs','Jadhav',55), 
(200013,'Vamanrao','Samakhs','Jadhav',39),
(200013,'Janvi','Vamanrao','Jadhav',35),
(200014,'Rohan','Jaganan','Shelke',30),
(200014,'Mohini','Rohan','Shelke',28),
(200014,'Renu','Rohan','Shelke',3)

---------------------------------------------------------
SELECT * FROM Distributer_details
SELECT * FROM Distributer_login
SELECT * FROM Customer_Details_Table
select * from Customer_family_details
