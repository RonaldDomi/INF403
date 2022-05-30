
DROP TABLE IF EXISTS Ecrit;
DROP TABLE IF EXISTS Possede;
DROP TABLE IF EXISTS OeuvreAudios;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Auteurs;
DROP TABLE IF EXISTS Audio_Types;

CREATE TABLE Auteurs (
	numero NUMBER(3, 0) NOT NULL PRIMARY KEY,
	nom VARCHAR(20) NOT NULL
);

CREATE TABLE Audio_Types(
	audiotype VARCHAR(20) NOT NULL PRIMARY KEY,
	longeur NUMBER(3,0),
	CONSTRAINT ck_audiotype_longeur CHECK (longeur > 0)
);

CREATE TABLE OeuvreAudios (
	numero NUMBER(3, 0) NOT NULL PRIMARY KEY,
	nom VARCHAR(20),
	prix NUMBER(8,2),-- NOT NULL,
    oeuvretype VARCHAR(20) NOT NULL,
	FOREIGN KEY (oeuvretype) REFERENCES Audio_Types (audiotype)
	ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT ck_oeuv_prix CHECK (prix >= 0)
);

CREATE TABLE Clients(
	numero NUMBER(3,0) NOT NULL PRIMARY KEY, 
	nom VARCHAR(20) NOT NULL,
	prenom VARCHAR(20), 
	date DATE
);

CREATE TABLE Ecrit (
	auteur_numero NUMBER(10) NOT NULL,
	oeuvre_numero NUMBER(10) NOT NULL,
	CONSTRAINT pk_aut_oeuv PRIMARY KEY (auteur_numero, oeuvre_numero),
	FOREIGN KEY (oeuvre_numero) REFERENCES OeuvreAudios(numero)
	ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (auteur_numero) REFERENCES Auteurs(numero)
	ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Possede (
	client_numero NUMBER(10) NOT NULL,
	oeuvre_numero NUMBER(10) NOT NULL,
	CONSTRAINT pk_cli_oeuv PRIMARY KEY (client_numero, oeuvre_numero),
	FOREIGN KEY (oeuvre_numero) REFERENCES OeuvreAudios(numero)
	ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (client_numero) REFERENCES Clients(numero)
	ON DELETE CASCADE ON UPDATE CASCADE
);

