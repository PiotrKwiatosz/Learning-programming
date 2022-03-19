# Zwraca nazwe klienta i numer powiazanych zamowien oraz wartość zamówien
# Rozwiazanie za pomoca ZAPYTANIA ZAGNIEZDZONEO

SELECT kl_nazwa, zam_numer,
	(SELECT SUM(cena_elem*ilosc)
    FROM ElementyZamowienia
    WHERE Zamowienia.zam_numer=ElementyZamowienia.zam_numer)
		AS wartosc_zam
FROM Klienci, Zamowienia
WHERE Klienci.kl_id = Zamowienia.kl_id
ORDER BY kl_nazwa, zam_numer;