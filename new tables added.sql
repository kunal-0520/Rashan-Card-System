-------------Item---------------
create table Item(Item_id int primary key not null identity(1,1),
Name varchar(25),Units varchar(25))

SELECT * FROM Item
------------Transactions----------
create table Transactions(Transaction_Id int primary key not null identity(1,1),
Ration_no int not null foreign key references Customer_Details_Table(Ration_no),First_Name varchar(50) not null,
Last_Name varchar(50),
Dates DATE,Distributer_id int not null foreign key references Distributer_details(Distributer_id))

select * from Transactions

-----------------Transaction_Details------------
create table Transaction_Details(Detail_Id int primary key not null identity(1,1),
Transaction_Id int not null foreign key references Transactions(Transaction_Id),
Item_id int not null foreign key references Item(Item_id),
Quantity varchar(25))

select * from Transaction_Details

----------------Inventory--------------------
create table Inventory(Inventory_id int primary key not null identity(1,1),
Distributer_id int not null foreign key references Distributer_details(Distributer_id),
Item_id int not null foreign key references Item(Item_id),quantity varchar(25))

select * from Inventory