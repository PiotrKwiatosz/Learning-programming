# Instrukcja tworzy tabele 'Zamowienia' sklada sie ona z 3 kolumn.

CREATE TABLE Zamowienia
(
	zam_numer	INTEGER		NOT NULL,
    zam_data	DATETIME	NOT NULL,
    kl_id		CHAR(10)	NOT NULL
);