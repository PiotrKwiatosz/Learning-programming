# Polaczone 2 wyniki zapytan slowen UNION:

# Pierwsze zapytanie - wszyscy klienci z woj. malopolskiego, mazowieckiego i wielkopolskiego
# Drugie zapytanie - wszyskie oddzialy 'Zabawa dla wszystkich' /niezaleznie od woj./

SELECT kl_nazwa, kl_kontakt, kl_email
FROM Klienci
WHERE kl_woj IN ('MAL', 'MAZ', 'WKP')
UNION
SELECT kl_nazwa, kl_kontakt, kl_email
FROM Klienci
WHERE kl_nazwa = 'Zabawa dla wszystkich';