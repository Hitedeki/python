  
USE [ApiFaces]
GO

CREATE TABLE Faces(
	ID int identity(1,1) primary key,
	idArquivo varchar(100),
	Vetor varchar(max),
	Centroid varchar(max),
	Grupo int,
	Nome varchar(100)
	
	
)

create table Cluster(
	id_cluster int identity(1,1) primary key,
	Centroid varchar(max)
	
