# Tutaj polecenie INSERT SELECT importuje wszystkie wiersze tabeli KlienciNowi do tabeli Klienci

INSERT INTO Klienci(kl_id,
					kl_kontakt,
					kl_email,
					kl_nazwa,
					kl_adres,
					kl_miasto,
					kl_woj,
					kl_kod,
					kl_kraj)
SELECT kl_id,
	kl_kontakt,
    kl_email,
    kl_nazwa,
    kl_adres,
    kl_miasto,
    kl_woj,
    kl_kod,
    kl_kraj
FROM KlienciNowi;