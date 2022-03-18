# Przykladowy kod zwraca produkty z zamowienia 20007 z 3 tabel

SELECT prod_nazwa, dost_nazwa, prod_cena, ilosc
FROM ElementyZamowienia, Dostawcy, Produkty
WHERE Dostawcy.dost_id = Produkty.dost_id
	AND ElementyZamowienia.prod_id = Produkty.prod_id
    AND zam_numer = 20007;
