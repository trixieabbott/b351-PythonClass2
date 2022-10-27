CREATE TABLE Student_T
    (StudentID                     NUMBER(5,0)        NOT NULL,
    StudentName                    VARCHAR2(25)        NOT NULL,
CONSTRAINT StudentID_PK PRIMARY KEY (StudentID));

CREATE TABLE Faculty_T
    (FacultyID                     NUMBER(5,0)        NOT NULL,
    FacultyName                    VARCHAR2(25)        NOT NULL,
CONSTRAINT FacultyID_PK PRIMARY KEY (FacultyID));

CREATE TABLE Course_T
    (CourseID                      VARCHAR2(10)        NOT NULL,
    CourseName                     VARCHAR2(25)        NOT NULL,
CONSTRAINT CourseID_PK PRIMARY KEY (CourseID));


--foreign keys are needed for following:

CREATE TABLE Qualified_T
    (FacultyID                     NUMBER(4,0)        NOT NULL,
    CourseID                       VARCHAR2(25)        NOT NULL,
    DateQualified                  DATE,
CONSTRAINT FacultyIDCourseID_PK PRIMARY KEY (FacultyID,CourseID),
CONSTRAINT FacultyID_FK FOREIGN KEY (FacultyID) REFERENCES Faculty_T(FacultyID),
CONSTRAINT CourseID_FK FOREIGN KEY (CourseID) REFERENCES Course_T(CourseID));

CREATE TABLE Section_T
    (SectionNo                     NUMBER(4,0)        NOT NULL,
    Semester                       VARCHAR2(25)        NOT NULL,
    CourseID                       VARCHAR2(25)        NOT NULL,
CONSTRAINT SectionNoSemesterCourseID_PK PRIMARY KEY (SectionNo,Semester,CourseID),
CONSTRAINT CourseID1_FK FOREIGN KEY (CourseID) REFERENCES Course_T(CourseID));

CREATE TABLE Registration_T
    (StudentID                     NUMBER(5,0)        NOT NULL,
    SectionNo                      NUMBER(4,0)        NOT NULL,
    Semester                       VARCHAR2(6)        NOT NULL,
CONSTRAINT StudentIDSectionNoSemeseter_PK PRIMARY KEY (StudentID,SectionNo,Semester),
CONSTRAINT StudentID1_FK FOREIGN KEY (StudentID) REFERENCES Student_T(StudentID));
--CONSTRAINT SectionNo1_FK FOREIGN KEY (SectionNo) REFERENCES Section_T(SectionNo)); 


--5
--A
INSERT INTO Student (StudentName, StudentID) VALUES('Lopez', '65798');
INSERT INTO Student VALUES(",'Lopez', '65798',",);
--B
DELETE FROM Student WHERE StudentID = '65798';
DELETE FROM Student WHERE LastName = 'Lopez';
--C
UPDATE Student SET CourseName = 'Introduction to Relational Databases' 
    WHERE CourseName = 'SM 4212';

--6
--A
SELECT StudentName FROM Student WHERE StudentID < 50000;
--B
SELECT FacultyName FROM Faculty WHERE FacultyID=4756:
--C
SELECT Min(SectionNO) FROM Section WHERE Semester=1-2008:


--7
--A
SELECT Count(*) FROM Section WHERE SectionNO=2714 and Semester=1-2008;
--B
SELECT Qualified.FacultyID, Qualified.CourseD, Qualified.DateQualified FROM Qualified WHERE
QUALIFIED.DateQualified>1993;


--8
--A
SELECT Course.ID, Section.[No], Registration.StudentID FROM Course, [Section], Registration
WHERE ((Course.ID)="DB212") AND ((Course.ID)="NT210");
--B
SELECT FacultyID, COUNT(*)AS TotalCount FROM Qualified WHERE CourselD NOT
IN('SA212' 'SD210') GROUP BY FacultyID;
--C
SELECT CourselD FROM Section WHERE Semester='1' AND Year='2008' AND CourselD NOT IN
(SELECT CourseD FROM Section WHERE Semester='2' AND Year='2008')

--9
--A
SELECT DISTINCT CourseD from SECTION;
--B
SELECT StudentName from STUDENT ORDER BY StudentName;
--C
SELECT StudentID, StudentName FROM Student WHERE StudentID IN (SELECT StudentID
FROM Registration WHERE SemesterID='1-2008' GROUP BY SectionNo):
--D
SELECT CourseD FROM Course GROUP BY CourselD;