# Zwracanie liczbe pozycji oraz sortowanie wg zam_pozycje

SELECT zam_numer, COUNT(*) AS zam_pozycje
FROM ElementyZamowienia
GROUP BY zam_numer
ORDER BY zam_pozycje;