# Pelne zlaczenie zewnetrzne

SELECT Klienci.kl_id, Zamowienia.zam_numer
FROM Klienci
FULL OUTER JOIN Zamowienia ON Zamowienia.kl_id = Klienci.kl_id;

