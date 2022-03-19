# Zwraca nazwe klienta i numer powiazanych zamowien

SELECT kl_nazwa, zam_numer
FROM Klienci
INNER JOIN Zamowienia ON Klienci.kl_id = Zamowienia.kl_id
ORDER BY kl_nazwa, zam_numer;