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

alter table consulta
	add column data date not null;

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

insert into quartos (ID, numero, consultorioID) values
	(6, 06, 1),
	(7, 07, 1),
	(8, 08, 1),
	(9, 09, 1),
	(10, 10, 1),
	(11, 11, 1),
	(12, 12, 1),
	(13, 13, 1),
	(14, 14, 1),
	(15, 15, 1),
	(16, 16, 1),
	(17, 17, 1),
	(18, 18, 1),
	(19, 19, 1),
	(20, 21, 1),
	(21, 22, 1),
	(22, 23, 1),
	(23, 24, 1),
	(24, 24, 1),
	(25, 25, 1),
	(26, 26, 1);


insert into lotacao (enfermeiraID, quartosID) values
	(1, 1),
	(1, 2),
	(1, 3),
	(2, 4),
	(2, 5);

insert into pacientes (ID, Nome, Cpf, Restricoes , quartosID) values
	(1, 'arthur balejo', '12312312312', null, 1),
	(2, 'gabriel cruz', '32132132132', 'alergia ozempic', 2),
	(3, 'isabela costa', '21321321321', null, 3),
	(4, 'eduardo zitske', '23123123123', 'alergia coach', 4);

insert into consulta (ID, pacientesID, medicaID, data) values
	(1, 1, 3, current_date),
	(2, 2, 3, current_date),
	(3, 3, 3, current_date),
	(4, 4, 3, current_date);

insert into receita (consultaID, pacientesID, medicaID, medicamento) values
	(1, 1, 3, 'silencio'),
	(2, 2, 3, 'tirzepatida');

select * from receita natural join pacientes p where receita.pacientesID = ID
	
	



