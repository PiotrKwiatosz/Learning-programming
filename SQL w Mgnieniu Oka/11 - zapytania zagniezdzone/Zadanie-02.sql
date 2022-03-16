# Ustalenie dat w ktorych zamowiono BR01

SELECT kl_id, zam_data
FROM Zamowienia
WHERE zam_numer IN	(SELECT zam_numer
				FROM ElementyZamowienia
				WHERE prod_id = 'BR01')
ORDER BY zam_data;
