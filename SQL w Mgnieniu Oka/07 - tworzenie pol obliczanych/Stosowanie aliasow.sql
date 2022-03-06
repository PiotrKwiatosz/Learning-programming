# Stosowanie aliasow dla wszystkich BD

# Wykorzystanie znaku +

SELECT RTRIM(dost_nazwa) + ' (' = RTRIM(dost_kraj) + ')'
		AS dost_tytul
FROM Dostawcy
ORDER BY dost_nazwa;

# Wykorzystanie znaku ||

SELECT RTRIM(dost_nazwa) || ' (' || RTRIM(dost_kraj) || ')'
		AS dost_tytul
FROM Dostawcy
ORDER BY dost_nazwa;

# Dla MySQL

SELECT Concat(RTrim(dost_nazwa), ' (', RTrim(dost_kraj), '(') AS dost_tytul
FROM Dostawcy
ORDER BY dost_nazwa;