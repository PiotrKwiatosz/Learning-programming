# Funkcja SUM() oblicza laczna cene za wszystkie sztuki

SELECT SUM(cena_elem*ilosc) AS laczna_cena
FROM ElementyZamowienia
WHERE zam_numer = 20005;