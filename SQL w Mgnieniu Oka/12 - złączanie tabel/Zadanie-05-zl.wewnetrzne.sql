# Zlaczenia z zadania z rozdz 10 gdzie trzeba bylo znalezc numery wszystkich zamowien o wartosci =1000
# Skladnia zlaczen wewnetrznych

SELECT kl_nazwa, SUM(cena_elem*ilosc) AS wydatki_razem
FROM Klienci, Zamowienia, ElementyZamowienia
WHERE Klienci.kl_id = Zamowienia.kl_id
	AND Zamowienia.zam_numer = ElementyZamowienia.zam_numer
GROUP BY kl_nazwa
HAVING SUM(cena_elem*ilosc) >= 1000
ORDER BY kl_nazwa;