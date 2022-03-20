# Prosty przyklad zlaczenia zewnetrznego ktory pobiera liste wszystkich klientow mawet tych ltprzy nie zlozyli zadnego zamowienia
# Pozostawienie wszystkich wierszy PRAWEJ tabeli

SELECT Klienci.kl_id, Zamowienia.zam_numer
FROM Klienci
RIGHT OUTER JOIN Zamowienia ON Zamowienia.kl_id = Klienci.kl_id;