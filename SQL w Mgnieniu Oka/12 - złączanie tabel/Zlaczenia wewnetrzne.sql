# Poniższa instrukcja spowoduje zwrocenie takich samych danych jak z 1 instrukcji "Tworzenie zlaczen" jednak zastosuje sie tu INNER

SELECT dost_nazwa, prod_nazwa, prod_cena
FROM Dostawcy
INNER JOIN Produkty ON Dostawcy.dost_id = Produkty.dost_id;
