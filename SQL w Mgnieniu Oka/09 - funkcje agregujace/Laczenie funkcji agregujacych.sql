# Cztery funkcje agregujace w jednym zapytaniu SELECT

SELECT COUNT(*) AS liczba_elementow,
	MIN(prod_cena) AS cena_min,
    MAX(prod_cena) AS cena_max,
    AVG(prod_cena) AS cena_sr
FROM Produkty;