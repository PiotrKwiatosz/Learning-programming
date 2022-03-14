# Zwracanie liczby wszystkich produktów oferowanych przez DLL01

SELECT COUNT(*) AS liczba_prod
FROM Produkty
WHERE dost_id = 'DLL01';