# Zmoddyfikowana instrukcja z zad.3 tak aby zwracala laczna liczbe zamowien kazdego produktu

SELECT prod_nazwa, COUNT(zam_numer) AS licza_zamowien
FROM Produkty
	LEFT OUTER JOIN ElementyZamowienia ON Produkty.prod_id = ElementyZamowienia.prod_id
GROUP BY prod_nazwa
ORDER BY prod_nazwa;