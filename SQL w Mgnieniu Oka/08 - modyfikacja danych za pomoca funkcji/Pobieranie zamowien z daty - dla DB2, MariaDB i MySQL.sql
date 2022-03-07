# Funkcja pobierajaca wszystkie zamowienia z roku 2020

SELECT zam_numer
FROM Zamowienia
WHERE YEAR(zam_data) = 2020;