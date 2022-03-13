# Srednia cena produktow oferowanych przez wybranego dostawce

SELECT AVG(prod_cena) AS sr_cena
FROM Produkty
WHERE dost_id = 'DLL01';