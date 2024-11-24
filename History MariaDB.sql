CREATE TABLE Empregados (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Cpf VARCHAR(100) UNIQUE,
    Tipo VARCHAR(100)    
);

create table Enfermeira (
	EmpregadosID int primary key references Empregados(ID),
	coren int
);

create table Medica (
	EmpregadosID int primary key references Empregados(ID),
	crm int not null,
	especialidade varchar(100) not null
);

create table consultorio (
	ID int primary key,
	cnpj varchar(100) unique
);

create table Quartos (
	ID int primary key,
	numero int not null,
	consultorioID int, 
	foreign key (consultorioID) references consultorio(ID)
);




