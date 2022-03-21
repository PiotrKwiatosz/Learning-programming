# Zmodyfikowana instrukcja ze zlaczeniem LEFT OUTER JOIN aby pobrac nazwy klientow, nawet tych co nie zlozyli zamowienia, i wszystkie numery zamowien kazdego klienta

SELECT kl_nazwa, zam_numer
FROM Klienci
LEFT OUTER JOIN Zamowienia ON Klienci.kl_id = Zamowienia.kl_id
ORDER BY kl_nazwa;