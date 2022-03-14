# Tworzenie grup przy pomocy GROUP BY. tworzenie 2 kolumn

SELECT dost_id, COUNT(*) AS liczba_prod
FROM Produkty
GROUP BY dost_id;