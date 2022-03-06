# Aliasy do zmiany nazwy pol tabeli w pobranych wynikach

SELECT dost_id, dost_nazwa AS dnazwa, dost_adres AS dadres, dost_miasto AS dmiasto
FROM Dostawcy
ORDER BY dnazwa;