# Grupowanie numerow zamowien wiekszych od 3

SELECT zam_numer, COUNT(*) AS elementy
FROM ElementyZamowienia
GROUP BY zam_numer
HAVING COUNT(*) >= 3;