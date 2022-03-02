SELECT zam_numer, prod_id, ilosc
FROM elementyzamowienia
WHERE (prod_id = 'BR01' OR 'BR02' OR 'BR03') AND ilosc >=100
ORDER BY prod_id AND ilosc;


 