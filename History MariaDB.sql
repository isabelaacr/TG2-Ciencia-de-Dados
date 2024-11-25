create table Empregados (
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

alter table Medica
modify column crm VARCHAR(100) not null;

alter table enfermeira 
modify column coren VARCHAR(100) not null;


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

use simpleclinic;

create table Pacientes(
	ID int primary key,
	Nome VARCHAR(100) NOT NULL,
    Cpf VARCHAR(100) UNIQUE,
    Restricoes VARCHAR(100),
    quartosID int,
    foreign key (quartosID) references Quartos(ID)
);

create table Lotacao (
    enfermeiraID INT NOT NULL,
    quartosID INT NOT NULL,
    PRIMARY KEY (enfermeiraID, quartosID),
    FOREIGN KEY (enfermeiraID) REFERENCES enfermeira(empregadosID),
    FOREIGN KEY (quartosID) REFERENCES quartos(ID)
);

create table Consulta (
	ID int not null,
	pacientesID int not null,
	medicaID int not null,
	primary key (ID, pacientesID, medicaID),
	foreign key (pacientesID) references pacientes(ID),
	foreign key (medicaID) references medica(EmpregadosID)	
);

create table receita (
	consultaID int not null,
	pacientesID int not null,
	medicaID int not null,
	medicamento varchar(100),
	primary key (consultaID, pacientesID, medicaID),
	foreign key (consultaID, pacientesID, medicaID) references Consulta(ID, pacientesID, medicaID)
);

insert into empregados (ID, Nome, Cpf, Tipo) values
	(1, 'lucinda silva', '11111111111', 'enfermeira'),
	(2, 'diamantina cruz', '22222222222', 'enfermeira'),
	(3, 'lagaia correia', '33333333333', 'medica');

insert into enfermeira (EmpregadosID, coren) values 
	(1, '123456 RS'),
	(2, '654321 SP');

insert into medica (EmpregadosID, crm, especialidade) values
	(3, 'CRM/RS 123456', 'Clinico Geral');

insert into consultorio (ID, cnpj) values
	(1, '12.123.123/0001-12');

insert into quartos (ID, numero, consultorioID) values
	(1, 01, 1),
	(2, 02, 1),
	(3, 03, 1),
	(4, 04, 1),
	(5, 05, 1);






