CREATE TABLE Publisher_T(
Publisher_ID				NUMBER(5),
City 					    	VARCHAR2(20),
Capital 					NUMBER(15)      not null,
CONSTRAINT Publisher_PK PRIMARY KEY (Publisher_ID));

CREATE TABLE Book_T( 
Book_ID				    	NUMBER(5),
Title					   	VARCHAR2(25)    not null,
Book_Language			VARCHAR2(15),
Genre					VARCHAR2(10)	not null, 
	CHECK (Genre IN ('Adventure','Fantasy','Horror','Science Fiction')),
Book_Rank				NUMBER(10),
Has_Digital_Version         	VARCHAR2(1) 		DEFAULT ‘N’,
	CHECK (Has_Digital_Version IN ('N','Y')),
Publisher_ID				NUMBER(5),
CONSTRAINT Book_PK PRIMARY KEY (Book_ID),
CONSTRAINT Book_FK FOREIGN KEY (Publisher_ID) REFERENCES Publisher_T (Publisher_ID)
ON DELETE SET NULL); 

CREATE TABLE Library_T(
Library_Name			VARCHAR2(15),
Library_Capacity			NUMBER(8) 		DEFAULT '1000',
Contact_Number			VARCHAR2(10)	not null,
Contact_Email			VARCHAR2(50),
Closing_Date				VARCHAR2(10),
    CHECK (Closing_Date IN ('Monday','Tuesday','Wednesday')),
CONSTRAINT Library_PK PRIMARY KEY (Library_Name));

CREATE TABLE Author_T(
Author_ID				VARCHAR2(4),
Author_Name				VARCHAR2(20)	not null unique,
Birthday				DATE		    DEFAULT DATE '1990-1-1' not null,
Experience				NUMBER(3),
		CHECK (Experience<100),
CONSTRAINT Author_PK PRIMARY KEY (Author_ID));

CREATE TABLE Collect_T(
Library_Name			VARCHAR2(15),
Book_ID					NUMBER(5),
Library_Cost 					NUMBER(10)	    not null,
CONSTRAINT Collect_PK PRIMARY KEY (Library_Name) REFERENCES Library_T(Library_Name),
ON DELETE SET NULL, 
CONSTRAINT Collect_PK PRIMARY KEY (Book_ID) REFERENCES Book_T(Book_ID),
ON DELETE CASCADE);

CREATE TABLE WrittenBy_T(
Book_ID					NUMBER(5),
Author_ID				VARCHAR2(4),
Work_Hour				NUMBER(6)	not null 		DEFAULT ‘100’,
CONSTRAINT WrittenBy_PK PRIMARY KEY (Author_ID) REFERENCES Author_T(Author_ID),
CONSTRAINT WrittenBy_PK PRIMARY KEY (Book_ID) REFERENCES Book_T(Book_ID),
ON DELETE CASCADE);