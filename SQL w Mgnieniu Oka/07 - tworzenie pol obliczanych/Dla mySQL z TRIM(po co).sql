# Stosowanie aliasow dla MySQL i nie wiem po co wyciecie spacji

SELECT Concat(RTrim(dost_nazwa), ' (', RTrim(dost_kraj), ')') AS dost_tytul
FROM Dostawcy
ORDER BY dost_nazwa;