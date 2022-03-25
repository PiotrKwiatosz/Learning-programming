# Unia przyjmuje pojedyczna klauzule ORDER BY po ostatnim zapytaniu SELECT

SELECT kl_nazwa, kl_kontakt, kl_email
FROM Klienci
WHERE kl_woj IN ('MAL', 'MAZ', 'WKP')
UNION
SELECT kl_nazwa, kl_kontakt, kl_email
FROM Klienci
WHERE kl_nazwa ='Zabawa dla wszystkich'
ORDER BY kl_nazwa, kl_kontakt;