# Pobiera liste wszystkich klientow wraz z liczba zlozonych przez nich zamowien
# Uzyto funkcji COUNT()

# Tem przyklad uzywa LEWEGO zlaczenia zewnetrznego co powoduje uwzglednienie wszystkich klientow nawet tych ktorzy nie zlozyli zadnego zamowienia

SELECT Klienci.kl_id,
	COUNT(Zamowienia.zam_numer) AS liczba_zam
FROM Klienci
	LEFT OUTER JOIN Zamowienia ON Klienci.kl_id = Zamowienia.kl_id
GROUP BY Klienci.kl_id;

