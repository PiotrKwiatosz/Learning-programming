# Pobieranie wszystkich nazw produktow a takze obliczona kolumne sprzedano ktora zawiera laczna ilosc sztuk sprzedana kazdego produktu

SELECT prod_nazwa,
	(SELECT SUM(ilosc)
    FROM ElementyZamowienia
    WHERE Produkty.prod_id = ElementyZamowienia.prod_id) AS sprzedano_sztuk
FROM Produkty;