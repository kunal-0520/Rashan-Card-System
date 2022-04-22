--------------------------------city------------------------------------
CREATE TABLE CITY(
CityID INT NOT NULL PRIMARY KEY IDENTITY(1,1),
City_Name VARCHAR(25))

INSERT INTO CITY VALUES('Nagpur'),('Amaravti'),('Akola'),('Wardha')
SELECT * FROM CITY

--------------------------------AREA----------------------------------
CREATE TABLE AREA(
AreaID INT NOT NULL PRIMARY KEY IDENTITY(1,1),
AreaName VARCHAR(25),
CityID INT FOREIGN KEY REFERENCES CITY(CityID))
INSERT INTO AREA VALUES('Pratap Nagar',1),('Subhash Nagar',1),('Rajkaml',2),('Aamba Nagri',2),('Gayatri nagar',3),('Tower chok',3),('Sambhaji Nagar',4)
SELECT * FROM AREA
------------------------------Distributer_details------------------------

CREATE TABLE Distributer_details(
Distributer_id INT NOT NULL PRIMARY KEY IDENTITY(1000,1),
First_name varchar(50) not null,
Middle_Name varchar(50) not null,
Last_name varchar(50) not null,
Area INT FOREIGN KEY REFERENCES AREA(AreaID),
City INT FOREIGN KEY REFERENCES CITY(CityID))

----------------------------Distributer_login---------------------------

CREATE TABLE Distributer_login(
Distributer_id int not null ,
Password varchar(50) not null, 
CONSTRAINT Distributer_id FOREIGN KEY (Distributer_id)
REFERENCES Distributer_details(Distributer_id))

-------------------------Customer_Details_Table-----------------------------

CREATE TABLE Customer_Details_Table(
Ration_no int not null primary key IDENTITY(200000,1),
Area INT FOREIGN KEY REFERENCES AREA(AreaID),
City INT FOREIGN KEY REFERENCES CITY(CityID),
Category varchar(10) check(Category in ('SC','OBC','ST','OPEN')),
Family_Income money,
Card_type varchar(10) check(Card_type in ('Yellow','Saffron','White')),
Distributer_Id int foreign key references Distributer_details(Distributer_Id)
)

-----------------------------Customer_family_details------------------------------
DROP TABLE Customer_family_details
CREATE TABLE Customer_family_details(
Ration_no int  foreign key references Customer_Details_Table(Ration_no),
First_Name varchar(50),
Middle_Name varchar(50),
Last_Name Varchar(50),
DOB DATE)

------------------------------------------------item-----------------------------------------
create table Item(
Item_id int primary key not null identity(1,1),
Name varchar(25),
Units varchar(25))


-----------------------------------------------Purchase------------------------------------------

CREATE TABLE Purchase(
PurchaseID INT NOT NULL PRIMARY KEY IDENTITY(1,1),
Purchase_Date DATE,
Distributer_Id int foreign key references Distributer_details(Distributer_Id),
Item_id INT foreign key references Item(Item_id),
Quantity Varchar(25))



--------------------------------------------------Allocation----------------------------------------------------------------
CREATE TABLE Allocation (
Allocation_ID INT NOT NULL PRIMARY KEY IDENTITY(1,1),
Ration_no int  foreign key references Customer_Details_Table(Ration_no),
Item_id INT foreign key references Item(Item_id),
Allocated_Quantity INT)

------------------------------------------------------Transactions----------------------------------------------------------------
create table Transactions(Transaction_Id int primary key not null identity(1,1),
Ration_no int not null foreign key references Customer_Details_Table(Ration_no),First_Name varchar(50) not null,
Last_Name varchar(50),
Dates DATE,Distributer_id int not null foreign key references Distributer_details(Distributer_id))

select * from Transactions




--------------------------------------------Transaction_Details--------------------------------------------------------------
create table Transaction_Details(Detail_Id int primary key not null identity(1,1),
Transaction_Id int not null foreign key references Transactions(Transaction_Id),
Item_id int not null foreign key references Item(Item_id),
Quantity varchar(25))

select * from Transaction_Details

---------------------------------------------------------------Inventory-----------------------------------------------------------------
create table Inventory(Inventory_id int primary key not null identity(1,1),
Distributer_id int not null foreign key references Distributer_details(Distributer_id),
Item_id int not null foreign key references Item(Item_id),quantity varchar(25))

