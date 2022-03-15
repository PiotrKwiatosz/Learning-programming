# Drugie zapytanie pobiera identyfikatory klientow ktorzy zlozyli zamowienie z 1 instrukcji

SELECT kl_id
FROM Zamowienia
WHERE zam_numer IN (20007, 20008);