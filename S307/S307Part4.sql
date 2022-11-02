--1 Write SQL retrieval commands for each of the following quries

--A
SELECT COURSEID,COURSENAME
FROM COURSE
WHERE COURSEID like 'ISM%';

--B
SELECT COURSEID 
FROM COURSE,QUALIFIED,FACULTY
WHERE FACULTY.FacultyName="berndt" and QUALIFIED.FacultyID=FACULTY.FacultyID;


--C
SELECT STUDENTNAME
FROM STUDENT,REGISTRATION,SECTION
WHERE REGISTRATION.SECTION='2714' and REGISTRATION.SectionNo=SECTION.SectionNo;


--2 Write an SQL query to answer the following question: Which instructors are qualified to teach ISM 3113?
SELECT FacultyName
FROM FACULTY,QUALIFIED
WHERE QUALIFIED.FacultyID=FACULTY. FacultyID
AND QUALIFIED.CourseD='ISM 3113';


--3 Write an SQL query to answer the following question: Is any instructor qualified to teach ISM 3113 and not qualified to teach ISM 4930?
SELECT FACULTY.FacultyName
FROM FACULTY, QUALIFIED
WHERE QUALIFIED.FacultyID=FACULTY. FacultyID
AND QUALIFIED.CourseID='ISM 3113'
AND NOT (QUALIFIED.CourseID='ISM 4930')

--4 Write SQL queries to answer the following questions:

--a. How many students were enrolled in section 2714 during semester I-2008?
SELECT COUNT (DISTINCT (StudentID))
FROM REGISTRATION
WHERE SectionNo = 2714
AND SEMESTER = 'I-2008'

-- b. How many students were enrolled in ISM 3113 duringsemester I-2008?
SELECT COUNT (DISTINCT (StudentID))
FROM SECTION, REGISTRATION
WHERE SECTION.SectionNO = REGISTRATION.SectionNO
AND CourseID = 'ISM 3113'
AND Semester = 'I-2008'

-- Write an SQL query to answer the followign question: which students were not enrolled in any courses during semester I 2008?
SELECT DISTINCT StudentID, STUDENTNAME
FROM STUDENT
WHERE NOT EXISTS (SELECT * FROM REGISTRATION WHERE STUDENT.StudentID = REGISTRATION.StudentID AND Semester='I-2008');