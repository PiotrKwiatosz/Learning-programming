# Filtrowanie grup z pomoca klauzuli WHERE
# Zapytanie powoduje wyświetlenie listy dostawcow z wiecej niz 1 produktem o cenie powyzej 10

SELECT dost_id, COUNT(*) AS liczba_prod
FROM Produkty
WHERE prod_cena >= 10
GROUP BY dost_id
HAVING COUNT(*) >= 2;