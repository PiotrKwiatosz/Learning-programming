# Funkcja robiaca login klientow z pierwszych liter danych kontaktowych, 3 pierwszych liter miasta i wszystko w duzych literach

SELECT kl_id, kl_kontakt, kl_miasto,
	CONCAT(UPPER(LEFT(kl_kontakt, 2)),
			UPPER(LEFT(kl_miasto, 3)))
				AS uzyt_login
FROM Klienci