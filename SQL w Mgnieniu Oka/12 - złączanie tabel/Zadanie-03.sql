# Instrukcja pobiera daty zamowienia BR01, tym razem przy uzyciu zlaczen

SELECT kl_id, zam_data
FROM Zamowienia, ElementyZamowienia
WHERE Zamowienia.zam_numer = ElementyZamowienia.zam_numer
	AND prod_id = 'BR01'
ORDER BY zam_data;