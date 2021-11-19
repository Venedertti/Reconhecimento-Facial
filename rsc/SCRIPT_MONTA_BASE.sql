# APS 2021 - 2° Semestre
# -> Banco de dados: Thiago Ramos de Oliveira

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
    EFEITO_ORAL		varchar(30) not null,
    EFEITO_DERMICO	varchar(40) not null,
    EFEITO_INALAR	varchar(30) not null,
    
    primary key(CD_AGRO)
);

create table TAPS_DOM_FUNC(
	CD_FUNC		int auto_increment not null,
    CPF_FUNC	varchar(20) not null,
    NOME		varchar(50) not null,
    NUMERO		varchar(15) not null,
    EMAIL		varchar(30) not null,
    CARGO 		varchar(15) not null,
    CD_NIVEL	int not null,
    
    primary key (CD_FUNC),
    foreign key (CD_NIVEL) references TAPS_DOM_NIVEL(CD_NIVEL)
);

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
	NOME_AGRO 		varchar(15) not null,
    
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

# taps_dom_agro
INSERT INTO TAPS_DOM_AGRO(CATEGORIA, DS_AGRO, EFEITO_ORAL, EFEITO_DERMICO, EFEITO_INALAR)
VALUES("CATEGORIA 1", "Extremamente toxico", "Fatal se ingerido", "Fatal em contato com a pele", "Fatal se inalado");

INSERT INTO TAPS_DOM_AGRO(CATEGORIA, DS_AGRO, EFEITO_ORAL, EFEITO_DERMICO, EFEITO_INALAR)
VALUES("CATEGORIA 2", "Altamente toxico", "Fatal se ingerido", "Fatal em contato com a pele", "Fatal se inalado");

INSERT INTO TAPS_DOM_AGRO(CATEGORIA, DS_AGRO, EFEITO_ORAL, EFEITO_DERMICO, EFEITO_INALAR)
VALUES("CATEGORIA 3", "Moderadamente toxico", "Toxico se ingerido", "Toxico em contato com a pele", "Toxico se inalado");

INSERT INTO TAPS_DOM_AGRO(CATEGORIA, DS_AGRO, EFEITO_ORAL, EFEITO_DERMICO, EFEITO_INALAR)
VALUES("CATEGORIA 4", "Pouco toxico", "Nocivo se ingerido", "Nocivo em contato com a pele", "Nocivo se inalado");

INSERT INTO TAPS_DOM_AGRO(CATEGORIA, DS_AGRO, EFEITO_ORAL, EFEITO_DERMICO, EFEITO_INALAR)
VALUES("CATEGORIA 5", "Improvavel causar dano agudo", "Pode ser perigoso se ingerido", "Pode ser perigoso em contato com a pele", 
		"Pode ser perigoso se inalado");

#popular tabelas quentes
# taps_hot_report
INSERT INTO TAPS_HOT_REPORT(NOME_EMPRE, ENDERECO_EMPRE, NUMERO_EMPRE, 
							DONO_EMPRE, GRAVIDADE, TIPO_DANO, CD_AGRO, QT_AGRO, NOME_AGRO)
VALUES("Imoboliaria Fachada", "Endereco 1, numero 1 - SP", "111111111","Guilherme Gomes David", 1, "Solo", 
		(SELECT CD_AGRO FROM TAPS_DOM_AGRO WHERE CATEGORIA = "CATEGORIA 1"), 1, "Agrotox de solo");

INSERT INTO TAPS_HOT_REPORT(NOME_EMPRE, ENDERECO_EMPRE, NUMERO_EMPRE, 
							DONO_EMPRE, GRAVIDADE, TIPO_DANO, CD_AGRO, QT_AGRO)
VALUES("Oficina Fachada", "Endereco 2, numero 2 - SP", "222222222","Bruno Amador", 2, "Mar", 
		(SELECT CD_AGRO FROM TAPS_DOM_AGRO WHERE CATEGORIA = "CATEGORIA 2"), 5, "Super Tox");

INSERT INTO TAPS_HOT_REPORT(NOME_EMPRE, ENDERECO_EMPRE, NUMERO_EMPRE, 
							DONO_EMPRE, GRAVIDADE, TIPO_DANO, CD_AGRO, QT_AGRO)
VALUES("Cafeteria Fachada", "Endereco 3, numero 3 - SP", "33333333333","Thiago Ramos de Oliveira", 3, "Fauna", 
		(SELECT CD_AGRO FROM TAPS_DOM_AGRO WHERE CATEGORIA = "CATEGORIA 3"), 8, "Hiper tox");