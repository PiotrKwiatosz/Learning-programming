SELECT zam_numer, prod_id, ilosc
FROM elementyzamowienia
WHERE ilosc >=100 AND prod_id = 'BR01' OR 'BR02' OR 'BR03'
ORDER BY prod_id AND ilosc;

 