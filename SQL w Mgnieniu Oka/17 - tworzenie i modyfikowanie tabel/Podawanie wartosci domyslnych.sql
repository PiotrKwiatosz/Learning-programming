# Instrukcja tworzy tabele 'ElementyZamowienia' zawierajaca ppszczegolne elementy zamowienia
# Podana jest wartosc domyslna DEFAULT 1 ktora to powoduje ze zostanie dana wartosc 1 dla kolumny ilosc ktorej w trakcjie dodawania wartosc nie zostanie okreslona

CREATE TABLE ElementyZamowienia
(
	zam_numer	INTEGER			NOT NULL,
    zam_element	INTEGER			NOT NULL,
    prod_id		CHAR(10)		NOT NULL,
    ilosc		INTEGER			NOT NULL DEFAULT 1,
    cena_elem	DECIMAL(8,2)	NOT NULL
);