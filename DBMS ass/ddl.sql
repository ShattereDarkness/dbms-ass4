drop database company_db;
create database company_db;
\c company_db

CREATE TABLE COMPANY
(
	CompanyID INT,
	Cname VARCHAR(10),
	Primary key(CompanyID)
);
CREATE TABLE DEPARTMENT
 (	Dname VARCHAR(15)  NOT NULL, 
	Mgr_ssn CHAR(9) ,
	CompanyID INT,
	DepartmentID Int,
	PRIMARY KEY (DepartmentID, CompanyID),
	-- UNIQUE (Dname),
	
	FOREIGN KEY (CompanyID) REFERENCES  COMPANY(CompanyID)
);
	
	
CREATE TABLE Employee
 (	Ssn CHAR(9) NOT NULL,
	Name VARCHAR(50) NOT NULL ,
	EmployeeID Int,  
	Address	 VARCHAR(50),
	Phone_number BIGINT,
	Job VARCHAR,
	Salary DECIMAL(10,2),
	DepartmentID INT NOT NULL,
	CompanyID INT NOT NULL,
	PRIMARY KEY (Ssn),
	FOREIGN KEY(DepartmentID, CompanyID) REFERENCES DEPARTMENT(DepartmentID, CompanyID)
);
CREATE TABLE TECHNOLOGIES
 (	
	TechID INT NOT NULL, 
	Tname VARCHAR(35) NOT NULL,
	CompanyID INT NOT NULL,
	DepartmentID INT NOT NULL,
	FOREIGN KEY(DepartmentID, CompanyID) REFERENCES DEPARTMENT(DepartmentID, CompanyID),
	PRIMARY KEY (TechID, DepartmentID, CompanyID)
);
CREATE TABLE Teaching
 (	
	Teacher_rating INT NOT NULL,
	Teacher_SSN CHAR(9) NOT NULL, 
	Techid INT ,
	DepartmentID INT NOT NULL,
	CompanyID INT NOT NULL,
	PRIMARY KEY (Techid, DepartmentID, CompanyID),
	FOREIGN KEY (Techid,DepartmentID, CompanyID) REFERENCES Technologies(TechID,DepartmentID,CompanyID),
	FOREIGN KEY(DepartmentID, CompanyID) REFERENCES DEPARTMENT(DepartmentID, CompanyID),
	FOREIGN KEY (Teacher_SSN) REFERENCES Employee(Ssn)
 );
CREATE TABLE Learning
 (	
	Student_score INT NOT NULL,
	Trainee_SSN CHAR(9) NOT NULL,
	Techid INT ,
	DepartmentID INT NOT NULL,
	CompanyID INT NOT NULL,
	PRIMARY KEY (Techid, DepartmentID, CompanyID, Trainee_SSN),
	constraint learning_techid_fkey
		FOREIGN KEY (Techid, DepartmentID, CompanyID) REFERENCES Teaching(TechID,DepartmentID,CompanyID)
		ON DELETE CASCADE,
		FOREIGN KEY(DepartmentID, CompanyID) REFERENCES DEPARTMENT(DepartmentID, CompanyID),
		FOREIGN KEY (Trainee_SSN) REFERENCES Employee(Ssn)
	);


--Add the following constraint after the data values have been entered into the tables.

--Alter Table Department Add Constraint Fkey_mgr_ssn FOREIGN KEY (Mgr_ssn) REFERENCES  EMPLOYEE(Ssn)