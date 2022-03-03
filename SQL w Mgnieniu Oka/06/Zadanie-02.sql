SELECT prod_nazwa, prod_opis
FROM Produkty
WHERE NOT prod_opis LIKE '%szmacianka%'
ORDER BY prod_nazwa;
 