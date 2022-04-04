# Instrukcja tworzy perspektywe 'ProduktyKlientow' ktora zlacza 3 tabele i zwraca liste wszystkich klientow ktorzy zamowili dowolny produkt

CREATE VIEW ProduktyKlientow AS
SELECT kl_nazwa, kl_kontakt, prod_id
FROM Klienci, Zamowienia, ElementyZamowienia
WHERE Klienci.kl_id = Zamowienia.kl_id
	AND ElementyZamowienia.zam_numer = Zamowienia.zam_numer;