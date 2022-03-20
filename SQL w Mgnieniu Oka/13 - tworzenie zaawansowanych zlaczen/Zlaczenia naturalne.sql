# Tworzenie zlaczen naturalnych gdzie eliminuje ono zwielokrotnienie wspolnych kolumn i zwracana jest tylko jedna kolumna
# Zlaczenie naturalne to mechanizm w ktorym pobierane sa tylko unikatowe kolumny

SELECT K.*, Z.zam_numer, Z.zam_data,

			E.prod_id, E.ilosc, E.cena_elem
FROM Klienci AS K, Zamowienia AS Z, ElementyZamowienia AS E
WHERE K.kl_id = Z.kl_id
	AND E.zam_numer = Z.zam_numer
    AND prod_id = 'RGAN01';