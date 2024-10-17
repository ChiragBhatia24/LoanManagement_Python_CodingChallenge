create database lmsfinal
use lmsfinal

 create table Customer(
 customer_id int identity(1,1) primary key,
 name varchar(255),
 email varchar(255),
 phone varchar(20),
 address varchar(255),
 credit_score int
 )

  create table Loan(
 loan_id int identity(1,1) primary key,
 customer_id int foreign key references Customer(customer_id),
 principal_amount int,
 interest_rate int,
 loan_term int,
 loan_type varchar(255),
 loan_status varchar(255),
 propertyAddress varchar(255),
 propertyValue int,
 carModel varchar(255),
 carValue int
 )