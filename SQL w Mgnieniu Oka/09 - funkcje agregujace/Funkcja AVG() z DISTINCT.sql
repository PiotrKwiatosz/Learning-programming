# Funkcja AVG() ale oblicza srednia tylko unikatowych wartosci

SELECT AVG(DISTINCT prod_cena) AS sr_cena
FROM Produkty
WHERE dost_id = 'DLL01';