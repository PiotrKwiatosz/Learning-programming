# Zlaczenie OUTER JOIN aby zlaczyc Produkty i ElementyZamowienia, instrukcja ma zwracac posortowana liste produktow i numerow zamowien

SELECT prod_nazwa, zam_numer
FROM Produkty
	LEFT OUTER JOIN ElementyZamowienia ON Produkty.prod_id = ElementyZamowienia.prod_id
ORDER BY prod_nazwa;