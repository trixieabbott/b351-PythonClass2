-- Trixie Abbott
-- S307 Homework3


-- added these so that I could continue to run this file
drop table Publisher_T cascade constraints;
drop table Book_T cascade constraints;
drop table Library_T cascade constraints;
drop table Author_T cascade constraints;
drop table Collect_T cascade constraints;
drop table Writtenby_T cascade constraints;


-- PART I

--1-- publisher
CREATE TABLE Publisher_T
	(Publisher_ID NUMBER(5),
	City VARCHAR2(20),
	Capital VARCHAR2(15) NOT NULL,
CONSTRAINT Publisher_PK PRIMARY KEY (Publisher_ID));
	

--2-- book
CREATE TABLE Book_T
	(Book_ID NUMBER(5),
	Title VARCHAR2(25) NOT NULL,
	BookLanguage VARCHAR2(15),
	Genre VARCHAR2(10) NOT NULL,
		CHECK (Genre IN ('Adventure', 'Fantasy', 'Horror', 'Science Fiction')),
	BookRank NUMBER(10),
	Has_Digital_Version VARCHAR2(1) DEFAULT 'N',
	Publisher_ID NUMBER(5),
CONSTRAINT Book_PK PRIMARY KEY (Book_ID),
CONSTRAINT Publisher_FK FOREIGN KEY (Publisher_ID) REFERENCES Publisher_T(Publisher_ID) ON DELETE SET NULL);
	

--3-- library
CREATE TABLE Library_T
	(Library_Name VARCHAR2(15),
	LibraryCapacity NUMBER(8) DEFAULT 1000,
	Contact_Number VARCHAR2(10) NOT NULL,
	Contact_Email VARCHAR2(50),
	Closing_Date VARCHAR2(10),
		CHECK (Closing_Date IN ('Monday', 'Tuesday', 'Wednesday')),
CONSTRAINT Library_PK PRIMARY KEY (Library_Name));


--4-- author
CREATE TABLE Author_T
	(Author_ID VARCHAR2(4),
	AuthorName VARCHAR2(20) NOT NULL UNIQUE,
	Birthday DATE DEFAULT to_date('01/01/1990','mm/dd/yyyy') NOT NULL,
	Experience NUMBER(3),
		CHECK (Experience < 100),
CONSTRAINT Author_PK PRIMARY KEY (Author_ID));


--5-- collect
CREATE TABLE Collect_T
	(Library_Name VARCHAR2(15),
	Book_ID NUMBER(5),
	CollectCost NUMBER(10) NOT NULL,
CONSTRAINT Collect_PK PRIMARY KEY (Library_Name,Book_ID),
CONSTRAINT Library_Name_FK FOREIGN KEY (Library_Name) REFERENCES Library_T(Library_Name),
CONSTRAINT Book_ID_FK FOREIGN KEY (Book_ID) REFERENCES Book_T(Book_ID) ON DELETE CASCADE);


--6-- writtenby
CREATE TABLE Writtenby_T
	(Book_ID NUMBER(5),
	Author_ID VARCHAR2(4),
	Work_Hour NUMBER(6) DEFAULT '100' NOT NULL,
CONSTRAINT WrittenBy_PK PRIMARY KEY (Book_ID,Author_ID),
CONSTRAINT Book_ID_FK1 FOREIGN KEY (Book_ID) REFERENCES Book_T(Book_ID) ON DELETE CASCADE,
CONSTRAINT Author_ID_FK FOREIGN KEY (Author_ID) REFERENCES Author_T(Author_ID) ON DELETE CASCADE);


--PART II

--1-- publisher
INSERT INTO Publisher_T (Publisher_ID, City, Capital) VALUES('11123', 'New York', '1500000');
INSERT INTO Publisher_T (Publisher_ID, City, Capital) VALUES('23456', 'New York', '9500000');
INSERT INTO Publisher_T (Publisher_ID, City, Capital) VALUES ('45678', 'London', '2000000');
INSERT INTO Publisher_T (Publisher_ID, City, Capital) VALUES ('55222', 'Paris', '3000000');

--2-- book
INSERT INTO Book_T (Book_ID, Title, BookLanguage, Genre, BookRank, Has_Digital_Version, Publisher_ID) VALUES ('14523', 'Clueless', 'English', 'Adventure', '500', 'Y', '11123');
INSERT INTO Book_T (Book_ID, Title, BookLanguage, Genre, BookRank, Has_Digital_Version, Publisher_ID) VALUES ('23445', 'One Kiss Less', 'English', 'Horror', '25', 'Y', '45678');
INSERT INTO Book_T (Book_ID, Title, BookLanguage, Genre, BookRank, Has_Digital_Version, Publisher_ID) VALUES ('25533', 'Circle', 'English', 'Adventure', '150', 'Y', '11123');
INSERT INTO Book_T (Book_ID, Title, BookLanguage, Genre, BookRank, Has_Digital_Version, Publisher_ID) VALUES ('15833', 'Rules and Roses', 'Spanish', 'Fantasy', '3', 'Y', '23456');
INSERT INTO Book_T (Book_ID, Title, BookLanguage, Genre, BookRank, Has_Digital_Version, Publisher_ID) VALUES ('78455', 'Silver Piano', 'Chinese', 'Fantasy', '15', 'N', '11123');


--3-- library
INSERT INTO Library_T (Library_Name, LibraryCapacity, Contact_Number, Contact_Email, Closing_Date) VALUES ('William Library', '500', '812100358', 'it@iu.edu', 'Monday');
INSERT INTO Library_T (Library_Name, LibraryCapacity, Contact_Number, Closing_Date) VALUES ('Herman Library', '3500', '812234567','Monday');
INSERT INTO Library_T (Library_Name, LibraryCapacity, Contact_Number, Contact_Email, Closing_Date) VALUES ('Lilly Library', '2500', '812889445', 'accounting@iu.edu', 'Tuesday');


--4-- author
INSERT INTO Author_T (Author_ID, AuthorName, Birthday, Experience) VALUES ('S125', 'Lisa Simpson', DATE '1965-09-09', '35');
INSERT INTO Author_T (Author_ID, AuthorName, Birthday, Experience) VALUES ('M302', 'Bart Simpson', DATE '2002-03-12', '3');
INSERT INTO Author_T (Author_ID, AuthorName, Birthday, Experience) VALUES ('X201', 'Michael Smith', DATE '1993-04-25', '2');
INSERT INTO Author_T (Author_ID, AuthorName, Birthday, Experience) VALUES ('S308', 'Maria Garcia', DATE '1982-12-31', '18');
INSERT INTO Author_T (Author_ID, AuthorName, Birthday) VALUES ('W115', 'Jane Austin', DATE '1975-12-16');


--5-- collect
INSERT INTO Collect_T (Library_Name, Book_ID, CollectCost) VALUES ('William Library', '15833', '3');
INSERT INTO Collect_T (Library_Name, Book_ID, CollectCost) VALUES ('William Library', '25533', '5');
INSERT INTO Collect_T (Library_Name, Book_ID, CollectCost) VALUES ('Herman Library', '15833', '2');
INSERT INTO Collect_T (Library_Name, Book_ID, CollectCost) VALUES ('Herman Library', '78455', '3');
INSERT INTO Collect_T (Library_Name, Book_ID, CollectCost) VALUES ('Herman Library', '14523', '6');
INSERT INTO Collect_T (Library_Name, Book_ID, CollectCost) VALUES ('Lilly Library', '15833', '8');

--6-- writtenby
INSERT INTO Writtenby_T (Book_ID, Author_ID, Work_Hour) VALUES ('14523', 'S125', '1500');
INSERT INTO Writtenby_T (Book_ID, Author_ID, Work_Hour) VALUES ('23445', 'S125', '800');
INSERT INTO Writtenby_T (Book_ID, Author_ID, Work_Hour) VALUES ('25533', 'M302', '350');
INSERT INTO Writtenby_T (Book_ID, Author_ID, Work_Hour) VALUES ('15833', 'X201', '125');
INSERT INTO Writtenby_T (Book_ID, Author_ID, Work_Hour) VALUES ('78455', 'S308', '130');



--PART III

--1--
SELECT *
FROM Publisher_T;


--2--
SELECT Book_ID, CollectCost + 5 AS "Final Cost"
FROM Collect_T;


--3--
SELECT Author_ID, Birthday
FROM Author_T
WHERE Author_ID LIKE 'S%' AND Birthday LIKE '%______65';


--4--
SELECT Author_ID, Experience
FROM Author_T
WHERE Author_ID LIKE '%3';


--5--
SELECT Library_Name
FROM Collect_T
WHERE CollectCost > 5
ORDER BY Library_Name;


--6--
SELECT UPPER(Library_Name)
FROM Library_T
WHERE Contact_Email IS NOT NULL AND LibraryCapacity > 2000;