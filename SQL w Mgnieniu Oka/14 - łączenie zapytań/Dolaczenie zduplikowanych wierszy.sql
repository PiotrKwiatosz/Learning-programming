# Jesli potrzebbe sa wszystkie wyniki nawet te zduplikowane uzywa sie UNION ALL

SELECT kl_nazwa, kl_kontakt, kl_email
FROM Klienci
WHERE kl_woj IN ('MAL', 'MAZ', 'WKP')
UNION ALL
SELECT kl_nazwa, kl_kontakt, kl_email
FROM Klienci
WHERE kl_nazwa ='Zabawa dla wszystkich';