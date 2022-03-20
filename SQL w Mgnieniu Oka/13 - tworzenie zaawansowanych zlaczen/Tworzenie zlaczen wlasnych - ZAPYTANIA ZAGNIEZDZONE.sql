# Nalezy wyslac email do wszystkich osob kontaktowych w firmie, w ktorej pracuje takze Danuta Sroka
# Korzystanie z zapytania zagniezdzonego

SELECT kl_id, kl_nazwa, kl_kontakt
FROM Klienci
WHERE kl_nazwa = (SELECT kl_nazwa
				FROM Klienci
                WHERE kl_kontakt = 'Danuta Sroka');