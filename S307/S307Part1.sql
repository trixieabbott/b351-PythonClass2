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