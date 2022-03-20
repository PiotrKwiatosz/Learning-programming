# Pobiera liste wszystkich klientow wraz z liczba zlozonych przez nich zamowien
# Uzyto funkcji COUNT()

SELECT Klienci.kl_id,
	COUNT(Zamowienia.zam_numer) AS liczba_zam
FROM Klienci
	INNER JOIN Zamowienia ON Klienci.kl_id = Zamowienia.kl_id
GROUP BY Klienci.kl_id;

