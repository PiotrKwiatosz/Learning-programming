# Instrukcja ktora zwraca i laczy prod_nazwa z kl_nazwa

SELECT prod_nazwa
FROM Produkty
UNION
SELECT kl_nazwa
FROM Klienci
ORDER BY prod_nazwa;