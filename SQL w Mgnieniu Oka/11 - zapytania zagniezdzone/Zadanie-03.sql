# Zwracanie email wszystkich klientow ktorzy kupili BR01

SELECT kl_email
FROM Klienci
WHERE kl_id IN (SELECT kl_id
				FROM Zamowienia
				WHERE zam_numer IN (SELECT zam_numer
									FROM ElementyZamowienia
									WHERE prod_id = 'BR01' ));
