# Filtrowanie grup bez klauzuli WHERE
# Zapytanie bez WHERE pobiera dodatkowy wiersz poniewaz dostawca DLL01 sprzedaje wszystkie 4 produkty o cenie ponizej 10

SELECT dost_id, COUNT(*) AS liczba_prod
FROM Produkty
GROUP BY dost_id
HAVING COUNT(*) >= 2;