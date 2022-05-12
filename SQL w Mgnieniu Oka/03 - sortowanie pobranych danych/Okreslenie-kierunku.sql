# Okreslanie kierunku wyswietlania ceny produktu - malejaca

SELECT prod_id, prod_cena, prod_nazwa
FROM Produkty
ORDER BY prod_cena DESC;