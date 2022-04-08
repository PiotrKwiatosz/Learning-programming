# Instrukcja definiuje klucz obcy

CREATE TABLE Zamowienia
	zam_numer	INTEGER		NOT NULL PRIMARY KEY,
    zam_data	DATETIME	NOT NULL,
    kl_id		CHAR(10)	NOT NULL REFERENCES Klienci(kl_id)
);