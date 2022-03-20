# Nalezy wyslac email do wszystkich osob kontaktowych w firmie, w ktorej pracuje takze Danuta Sroka
# Korzystanie ze ZLACZEN

SELECT k1.kl_id, k1.kl_nazwa, k1.kl_kontakt
FROM Klienci AS k1, Klienci AS k2
WHERE k1.kl_nazwa = k2.kl_nazwa
	AND k2.kl_kontakt = 'Danuta Sroka';