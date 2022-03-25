# Instrukcja obejmujaca 2 instrukcje SELECT pobierajaca prod_id i ilosc. Filtrowanie w 1 ma zwracac tylko ilosc = 100 a w 2 wiersze z prod_id zaczynajacymi sie od BNBG

SELECT prod_id, ilosc
FROM ElementyZamowienia
WHERE ilosc = 100
	OR prod_id LIKE 'BNBG%'
ORDER BY prod_id;