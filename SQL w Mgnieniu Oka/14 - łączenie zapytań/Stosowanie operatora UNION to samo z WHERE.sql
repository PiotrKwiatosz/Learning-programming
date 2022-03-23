# Dla porownania wynikow z cw.1. podane jest zapytanie dajace te same wyniki ale korzystajac z WHERE

SELECT kl_nazwa, kl_kontakt, kl_email
FROM Klienci
WHERE kl_woj IN ('MAL', 'MAZ', 'WKP')
	OR kl_nazwa = 'Zabawa dla wszystkich';