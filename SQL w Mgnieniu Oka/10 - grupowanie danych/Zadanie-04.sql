# Pokazywanie najlepszych klientow ktorych laczna cena wynosii 1000

SELECT zam_numer, SUM(cena_elem*ilosc) AS cena_w_sumie
FROM ElementyZamowienia
GROUP BY zam_numer
HAVING SUM(cena_elem*ilosc) >= 1000;