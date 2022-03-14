# Pokazywanie najlepszych klientow

SELECT zam_numer
FROM ElementyZamowienia
GROUP BY zam_numer
HAVING SUM(ilosc) >= 100
ORDER BY zam_numer;