# Zwracanie najtansze produkty od kazdego producenta

SELECT dost_id, MIN(prod_cena) AS najtanszy_prod
FROM Produkty
GROUP BY dost_id
ORDER BY najtanszy_prod;