# Modyfikacja rekordow tabeli 'Dostawcy' dodajac do nich adres witryny

UPDATE Dostawcy
SET dost_witryna = 'www.zabawkolando.pl'
WHERE dost_id = 'DLL01';