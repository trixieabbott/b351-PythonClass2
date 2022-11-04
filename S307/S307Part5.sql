-- 7.32
ALTER TABLE STUDENT_T
ADD MathScore NUMBER(3);

--7.33
ALTER TABLE TUTOR_T
ADD Subject VARCHAR(50)
CHECK (Subject in ('Reading','Math','ESL'));

--7.34
--If a tutor wants to tutor in more than one subject, there needs to be 3 other entities, tutorsubject, and subject that is tied to tutors and students
-- we could utilize the follow commands to create these

CREATE TABLE Subject(SubjectID number(5) NOT NULL PRIMARY KEY,
                        SubjectName Varchar2(15) NOT NULL);
CREATE TABLE Tutor(TutorID number(5) NOT NULL PRIMARY KEY,
                    Status Varchar2(15) NOT NULL);
                    
CREATE TABLE TutorSUBJECT(TutorID number(5) REFERENCES Tutor(TutorID),
                            CerDate date, PRIMARY KEY(TutorID, SubjectID));

ALTER TABLE MatchHistory
    ADD COLUMN SubjectID Number(5);


--7.35
SELECT *
FROM( SELECTSELECT MatchHistory.MatchID, MatchHistory.EndDate,MatchHistory.TutorID, TutorReport.Month
FROM MatchHistory LEFT JOIN TutorReport ON MatchHistory.MatchID = TutorReport.MatchID

WHERE (((MatchHistory.EndDate) IS NULL)) OR (((MatchHistory.EndDate)>6/30/2008) AND
((TutorReport.Month) Is Null))) AS Q6

WHERE (((Q6.Month) IS NULL)) OR
(((Q6.Month)>=6/30/2008 And (Q6.Month) NOT BETWEEN 7/1/2008 And 7/31/2008));
