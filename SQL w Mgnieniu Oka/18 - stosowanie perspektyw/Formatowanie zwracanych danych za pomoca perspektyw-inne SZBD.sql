# Tworzenie perspektywy ktora daje dane adresowe wraz z krajem
# Wersja dla innych SQL (SQLite, SQL Server, DB9)

CREATE VIEW LokalizacjeKlientow AS
SELECT RTRIM(dost_nazwa) + ' (' + RTRIM(dost_kraj) + ')'
	AS dost_tytul
FROM Dostawcy;

CREATE VIEW LokalizacjeKlientow AS
SELECT RTRIM(dost_nazwa) || ' (' || RTRIM(dost_kraj) || ')'
	AS dost_tytul
FROM Dostawcy;