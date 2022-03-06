# Dawanie tylko produktow ktore maja w opisie "szmmackanka" i "Rybka" #
SELECT prod_nazwa, prod_opis
FROM Produkty
WHERE prod_opis LIKE '%szmacianka%' AND prod_opis LIKE '%Rybka%';
 