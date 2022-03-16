# Trzeba wyswietlic laczna liczbe zamowien zlozonych przez kazdego klienta, zamowienia znajduja sie w tabeli "Zamowienia" wraz z odpowiednim id klienta

SELECT kl_nazwa,
		kl_woj,
			(SELECT COUNT(*)
            FROM Zamowienia
            WHERE Zamowienia.kl_id = Klienci.kl_id) AS zamowienia
FROM Klienci
ORDER BY kl_nazwa;