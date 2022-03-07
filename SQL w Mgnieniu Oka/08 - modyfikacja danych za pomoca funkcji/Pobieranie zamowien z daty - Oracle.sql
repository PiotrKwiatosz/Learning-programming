# Funkcja pobierajaca wszystkie zamowienia z roku 2020

SELECT zam_numer
FROM Zamowienia
WHERE zam_data BETWEEN to_date('2020-01-01', 'yyyy-mm-dd') 
	AND to_date('2020-12-31', 'yyyy-mm-dd');