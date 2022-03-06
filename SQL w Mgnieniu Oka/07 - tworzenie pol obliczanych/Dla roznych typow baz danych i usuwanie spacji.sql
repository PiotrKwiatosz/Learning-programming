# Konkatencja (scalanie) pol  i usuwanie spacji

# Wykorzystanie znaku +

SELECT RTRIM(dost_nazwa) + ' (' = RTRIM(dost_kraj) + ')'
FROM Dostawcy
ORDER BY dost_nazwa;

# Wykorzystanie znaku ||

SELECT RTRIM(dost_nazwa) || ' (' || RTRIM(dost_kraj) || ')'
FROM Dostawcy
ORDER BY dost_nazwa;