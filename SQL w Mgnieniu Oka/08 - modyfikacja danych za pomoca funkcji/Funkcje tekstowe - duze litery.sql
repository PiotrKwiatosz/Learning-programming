# Konwertowanie tekstu na duze litery 

SELECT dost_nazwa, UPPER(dost_nazwa) AS dost_nazwa_duze
FROM Dostawcy
ORDER BY dost_nazwa;