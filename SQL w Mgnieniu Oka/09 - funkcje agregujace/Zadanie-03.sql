# Cena najdrozszego produktu ktory kosztuje nie wiecej niz 10

SELECT MAX(prod_cena) AS max_cena, prod_nazwa
FROM Produkty
WHERE prod_cena <= 10;