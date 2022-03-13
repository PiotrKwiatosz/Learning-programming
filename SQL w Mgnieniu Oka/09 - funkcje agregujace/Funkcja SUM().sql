# Funkcja SUM() zwraca laczna liczbe sztuk elementow w okreslonym zamowienu

SELECT SUM(ilosc) AS elementy_zamowienia
FROM ElementyZamowienia
WHERE zam_numer = 20005;