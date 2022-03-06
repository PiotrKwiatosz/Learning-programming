# Konkatencja (scalanie) pol

# Wykorzystanie znaku +

SELECT dost_nazwa + ' (' = dost_kraj + ')'
FROM Dostawcy
ORDER BY dost_nazwa;

# Wykorzystanie znaku ||

SELECT dost_nazwa || ' (' || dost_kraj || ')'
FROM Dostawcy
ORDER BY dost_nazwa;

# Dla MySQL

SELECT Concat(dost_nazwa, ' (', dost_kraj, ')')
FROM Dostawcy
ORDER BY dost_nazwa;