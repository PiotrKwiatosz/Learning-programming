# Utworzenie perspektywy KlienciZZamowieniami zawierajacej wszystkie kolumny z tabeli Klienci, ale obejmujaca tylko wiersze klientow co zlozyli jakies zamowienie.

CREATE VIEW KlienciZZamowieniami AS
SELECT Klienci.kl_id,
		Klienci.kl_nazwa,
        Klienci.kl_adres,
        Klienci.kl_miasto,
        Klienci.kl_woj,
        Klienci.kl_kod,
        Klienci.kl_kraj,
        Klienci.kl_kontakt,
        Klienci.kl_email
FROM Klienci
JOIN Zamowienia ON Klienci.kl_id = Zamowienia.kl_id;