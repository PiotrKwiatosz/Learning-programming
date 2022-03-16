# Zwracanie listy klientow ktorzy kupili prod o cenie >= 10

SELECT kl_id
FROM Zamowienia
	WHERE zam_numer IN (SELECT zam_numer
				FROM ElementyZamowienia
				WHERE cena_elem >= 10);
