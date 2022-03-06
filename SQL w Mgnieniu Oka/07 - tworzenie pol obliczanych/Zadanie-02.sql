# Wszystkie produkty z rabatem 10%

SELECT prod_id, prod_cena, Concat(prod_cena*0.9) AS cena_wyprz
FROM Produkty
ORDER BY cena_wyprz;