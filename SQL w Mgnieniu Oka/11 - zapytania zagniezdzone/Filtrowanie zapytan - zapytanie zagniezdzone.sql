# Polaczenie obu zapytan i tworzy sie zapytanie zagniezdzone

SELECT kl_id
FROM Zamowienia
WHERE zam_numer IN (SELECT zam_numer
					FROM ElementyZamowienia
					WHERE prod_id = 'RGAN01');