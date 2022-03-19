# Zwraca nazwe klienta i numer powiazanych zamowien oraz wartość zamówien
# Rozwiazanie za pomoca ZAPYTANIA ZAGNIEZDZONEO

SELECT kl_nazwa,
	Zamowienia.zam_numer,
	SUM(cena_elem*ilosc) AS wartosc_zam
FROM Klienci, Zamowienia, ElementyZamowienia
WHERE Klienci.kl_id = Zamowienia.kl_id
	AND Zamowienia.zam_numer = ElementyZamowienia.zam_numer
GROUP BY kl_nazwa, Zamowienia.zam_numer
ORDER BY kl_nazwa, zam_numer;