#APS 2021 - 2° Semestre
#Banco de dados: Thiago Ramos de Oliveira

#create database
create database aps_agrosafe;
use aps_agrosafe;

#create dom tables
create table TAPS_DOM_NIVEL(
	CD_NIVEL int primary key not null,
    DS_NIVEL varchar(20) not null
);

create table TAPS_DOM_AGRO(
	CD_AGRO 		int auto_increment not null,
    CATEGORIA 		varchar(20) not null,
    DS_AGRO 		varchar(30) not null,
    EFEITO_ORAL		varchar(20) not null,
    EFEITO_DERMICO	varchar(20) not null,
    EFEITO_INALAR	varchar(20) not null,
    
    primary key(CD_AGRO)
);

create table TAPS_DOM_FUNC(
	CD_FUNC		int auto_increment not null,
    CPF_FUNC	varchar(11) not null,
    NOME		varchar(50) not null,
    NUMERO		varchar(15) not null,
    EMAIL		varchar(30) not null,
    CARGO 		varchar(15) not null,
    CD_NIVEL	int not null,
    IDENTIFIC	varchar(50),
    
    primary key (CD_FUNC),
    foreign key (CD_NIVEL) references TAPS_DOM_NIVEL(CD_NIVEL)
);

#create ass tables
create table TAPS_ASS_FUNC_NIVEL(
	CD_FUNC		int not null,
    CD_NIVEL	int not null,

	foreign key(CD_FUNC) references TAPS_DOM_FUNC(CD_FUNC),
    foreign key (CD_NIVEL) references TAPS_DOM_NIVEL(CD_NIVEL)
);

show tables;

#create hot tables
create table TAPS_HOT_REPORT(
	CD_REPORT		int auto_increment not null,
    NOME_EMPRE		varchar(30) not null,
    ENDERECO_EMPRE	varchar(60) not null,
    NUMERO_EMPRE	varchar(15) not null,
    DONO_EMPRE		varchar(50) not null,
    GRAVIDADE		int not null,
    TIPO_DANO		varchar(15) not null,
    CD_AGRO			int not null,
    QT_AGRO			int not null,

	primary key(CD_REPORT),
    foreign key(CD_AGRO) references TAPS_DOM_AGRO(CD_AGRO)
);

#popular tabelas dom
# taps_dom_nivel
INSERT INTO TAPS_DOM_NIVEL(CD_NIVEL, DS_NIVEL)
VALUES(1, "Nivel 1");
INSERT INTO TAPS_DOM_NIVEL(CD_NIVEL, DS_NIVEL)
VALUES(2, "Nivel 2");
INSERT INTO TAPS_DOM_NIVEL(CD_NIVEL, DS_NIVEL)
VALUES(3, "Nivel 3");

