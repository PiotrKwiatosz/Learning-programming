# Instrukcja z zadania 3 rozdz 11 jednak tym razem z uzyciem skladni INNER JOIN

SELECT kl_email
FROM Klienci
INNER JOIN Zamowienia ON Klienci.kl_id = Zamowienia.kl_id
INNER JOIN ElementyZamowienia ON Zamowienia.zam_numer = ElementyZamowienia.zam_numer
WHERE prod_id = 'BR01';