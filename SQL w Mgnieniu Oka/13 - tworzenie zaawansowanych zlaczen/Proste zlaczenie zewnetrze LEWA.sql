# Prosty przyklad zlaczenia zewnetrznego ktory pobiera liste wszystkich klientow mawet tych ltprzy nie zlozyli zadnego zamowienia
# Pozostawienie wszystkich wierszy LEWEJ tabeli

SELECT Klienci.kl_id, Zamowienia.zam_numer
FROM Klienci
LEFT OUTER JOIN Zamowienia ON Zamowienia.kl_id = Klienci.kl_id;