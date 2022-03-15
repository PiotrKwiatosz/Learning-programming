# Pierwsza instrukcja pobiera kolumne zam_numer dla wszystkich elementow gdzie prod_id wynosi RGAN01

SELECT zam_numer
FROM ElementyZamowienia
WHERE prod_id = 'RGAN01';