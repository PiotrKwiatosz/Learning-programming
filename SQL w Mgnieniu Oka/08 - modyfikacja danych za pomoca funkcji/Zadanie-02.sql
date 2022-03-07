# Zwracanie numer i daty zamowien ze stycznia 2020

SELECT zam_numer, zam_data
FROM Zamowienia
WHERE MONTH(zam_data) = 1 AND YEAR(zam_data) = 2020
ORDER BY zam_data;