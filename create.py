CREATE TABLE TestesFaces(
	ID int identity(1,1) primary key,
	Nome varchar(100),
	CPF varchar(15),
	Vetor varchar(max)
)


CREATE TABLE Faces(
	ID int identity(1,1) primary key,
	idArquivo varchar(100),
	status varchar(100),
	Vetor varchar(max)
)
