# Tworzenie perspektywy ktora daje dane adresowe wraz z krajem
# Wersja dla MySQL

CREATE VIEW LokalizacjeKlientow AS
SELECT Concat(dost_nazwa, ' (', dost_kraj, ')')
	AS dost_tytul
FROM Dostawcy;