# Aktualizacja poprzez usuwanie kolumny poprzez wprowadzenie wartosci NULL

UPDATE Klienci
SET kl_email = NULL
WHERE kl_id = '1000000005';