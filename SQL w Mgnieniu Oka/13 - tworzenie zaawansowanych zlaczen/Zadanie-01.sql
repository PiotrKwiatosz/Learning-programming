# Instrukcja ze zlaczeniem INNER JOIN aby pobrac nazwy klientow i wszystkie numery zamowien kazdego klienta

SELECT kl_nazwa, zam_numer
FROM Klienci
INNER JOIN Zamowienia ON Klienci.kl_id = Zamowienia.kl_id
ORDER BY kl_nazwa;