# Tworzenie perspektywy fktora jest z instrukcja z rozdz. 7.. Pobiera ona elementy wybranego zamowienia wraz z pelna cena za wszystkie sztuki danego elementu

CREATE VIEW WartoscElementowZamowienia AS
SELECT zam_numer,
		prod_id,
        ilosc,
        cena_elem,
        ilosc*cena_elem AS wartosc
FROM ElementyZamowienia;