# Instrukcja tworzy tabele 'Produkty'

CREATE TABLE Produkty
(
	prod_id		CHAR(10)		NOT NULL,
    dost_id		CHAR(10)		NOT NULL,
    prod_nazwa	CHAR(254)		NOT NULL,
    prod_cena	DECIMAL(8,2)	NOT NULL,
    prod_opis	VARCHAR(1000)	NULL
);