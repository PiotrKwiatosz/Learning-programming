# Stosowanie aliasow dla baz danych

# Uzycie +
SELECT RTrim(dost_nazwa) + ' (', RTrim(dost_kraj) + ')'
		AS dost_tytul
FROM Dostawcy
ORDER BY dost_nazwa;

# Uzycie ||
SELECT RTrim(dost_nazwa) || ' (', RTrim(dost_kraj) || ')'
		AS dost_tytul
FROM Dostawcy
ORDER BY dost_nazwa;