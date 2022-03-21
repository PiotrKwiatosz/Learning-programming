# Instrukcja wyswietla dostawcow i liczbe produktow oferowanych przez kazdego z nich, pokazuje takze dostawcow ktorzy nie oferuja zadnych produktow

SELECT Dostawcy.dost_id, COUNT(prod_id)
FROM Dostawcy
	LEFT OUTER JOIN Produkty ON Dostawcy.dost_id = Produkty.dost_id
GROUP BY Dostawcy.dost_id;