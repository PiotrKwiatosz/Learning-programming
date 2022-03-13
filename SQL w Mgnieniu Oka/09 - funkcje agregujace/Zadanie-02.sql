# Laczna liczba sprzedanych produktow BR01

SELECT SUM(ilosc) AS liczba_sprzedanych
FROM ElementyZamowienia
WHERE prod_id = 'BR01';