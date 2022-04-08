# To ograniczenie umozliwia wstawianie tylko takich danych w kolumnie 'ilosc' posiadajacych wartosc wieksza niz 0

CREATE TABLE ElementyZamowienia
(
	zam_numer	INTEGER		NOT NULL,
    zam_element	INTEGER		NOT NULL,
    prod_id		CHAR(10)	NOT NULL,
    ilosc		INTEGER		NOT NULL CHECK (ilosc > 0),
    cena_elem	MONEY		NOT NULL
);