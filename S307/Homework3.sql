CREATE TABLE Publisher_T
    (Publisher_id                  NUMBER(5),
    City                           VARCHAR2(20),
    Capital                        Number(15)     NOT NULL,
CONSTRAINT Publisher_id_PK PRIMARY KEY (Publisher_id));

CREATE TABLE Book_T
    (Book_ID                        NUMBER(5),
    Title                           VARCHAR2(25)        NOT NULL,
    Book_Language                   VARCHAR2(15),
    Genre                           VARCHAR2(10)    NOT NULL CHECK (Genre IN ('Adventure', 'Fantasy', 'Horror', 'Science Fiction')),
    Book_Rank                       NUMBER(10),
    Has_digital_version             VARCHAR2(1) DEFAULT 'N' CHECK (Has_digital_version IN ('Y', 'N')),
    Publisher_id                    NUMBER(5),
CONSTRAINT Book_ID_PK PRIMARY KEY (Book_ID)
CONSTRAINT Publisher_id_FK FOREIGN KEY (Publisher_id) REFERENCES Publisher_T (Publisher_id) ON DELETE SET NULL);

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