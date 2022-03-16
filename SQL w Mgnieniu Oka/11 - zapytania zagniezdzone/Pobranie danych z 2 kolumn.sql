# Pobieranie kontaktow klientow ktorzy zamowili dane produkty z zamowienia id=RGAN01

SELECT kl_nazwa, kl_kontakt
FROM Klienci
WHERE kl_id IN (SELECT kl_id
				FROM Zamowienia
				WHERE zam_numer IN (SELECT zam_numer
									FROM ElementyZamowienia
                                    WHERE prod_id = 'RGAN01'));