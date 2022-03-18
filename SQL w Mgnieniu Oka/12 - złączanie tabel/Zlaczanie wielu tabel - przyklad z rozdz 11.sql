# Przyklad z rozdzialu 11 przy wykorzystaniu zlaczen

SELECT kl_nazwa, kl_kontakt
FROM Klienci, Zamowienia, ElementyZamowienia
WHERE Klienci.kl_id = Zamowienia.kl_id
	AND ElementyZamowienia.zam_numer = Zamowienia.zam_numer
    AND prod_id = 'RGAN01';