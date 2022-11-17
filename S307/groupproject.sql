
--Trixie SQL Table Creations

--Artist Table
CREATE TABLE Artist_T
(AristID		NUMBER(8,0)	    NOT NULL UNIQUE,
ArtistName		VARCHAR2(16)    NOT NULL,
EmailAddress	VARCHAR2(50)	NOT NULL,
CONSTRAINT Artist_PK PRIMARY KEY(ArtistID));

--Singer Table (subytpe of Artist)
CREATE TABLE Singer_T
(AristID		    NUMBER(8,0)	    NOT NULL UNIQUE,
ManagementID	    NUMBER(8,0)    NOT NULL,
NumberOfListeners	NUMBER(100,0),              --which datatype should be used here?
NumberofAlbums	    NUMBER(100,0)    NOT NULL,  --which datatype should be used here?
TourDates	        VARCHAR2(50),               --which datatype should be used here?
SongTitle	        VARCHAR2(50)    NOT NULL,   --how does this attribute work? one song? multiple?
CONSTRAINT Singer_PK PRIMARY KEY(ArtistID),
CONSTRAINT Singer_FK FOREIGN KEY(AristID) REFERENCES Artist_T(ArtistID));

--PodcastCreator Table (subytpe of Artist)
CREATE TABLE PodcastCreator_T
(AristID		    NUMBER(8,0)	    NOT NULL UNIQUE,
ProductionID	    NUMBER(8,0)    NOT NULL,
PodcastName	        VARCHAR2(50)	NOT NULL,
NumberofFollowers   NUMBER(100,0),            --which datatype should be used here?
PodcastID   	    NUMBER(8,0)    NOT NULL,  --we decided we would use ArtistID instead, why is this neccesary
CONSTRAINT PodcastCreator_PK PRIMARY KEY(ArtistID),
CONSTRAINT PodcastCreator_FK FOREIGN KEY(AristID) REFERENCES Artist_T(ArtistID));


--Album Table
CREATE TABLE Album_T
(AlbumID		    NUMBER(8,0)	    NOT NULL UNIQUE,
NumberofSongs        NUMBER(8,0)     NOT NULL,            --which datatype should be used here?
ArtistName	        VARCHAR2(50)	NOT NULL,
ReleaseDate         DATE            NOT NULL,            
CONSTRAINT Album_PK PRIMARY KEY(AlbumID));

--Song Table
CREATE TABLE Song_T
(SongID		        NUMBER(8,0)	    NOT NULL UNIQUE,
AlbumID             NUMBER(8,0)     NOT NULL, 
ArtistID	        NUMBER(8,0)	    NOT NULL,
SongName            VARCHAR2(50)    NOT NULL,   
NumberofStreams     NUMBER(100,0)     NOT NULL,            --which datatype should be used here?
CONSTRAINT Song_PK PRIMARY KEY(SongID),
CONSTRAINT Song_FK1 FOREIGN KEY(AlbumID) REFERENCES Album_T(AlbumID),
CONSTRAINT Song_FK2 FOREIGN KEY(ArtistID) REFERENCES Artist_T(ArtistID));
