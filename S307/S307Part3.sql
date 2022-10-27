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