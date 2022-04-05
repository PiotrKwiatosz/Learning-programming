# Wstawianie nowej pozycji do tabeli 'Zamowienia'

CREATE PROCEDURE NoweZamowienie @kl_id CHAR(10)
AS
-- Deklarowanie zmiennej dla numeru zamowienia
DECLARE @zam_numer INTEGER
-- Pobranie najwiekszego numeru zamowienia
SELECT @zam_numer=MAX(zam_numer)
FROM Zamowienia
-- Okreslenie nastepnego numeru zamowienia
SELECT @zam_numer=@zam_numer+1
-- Wstawienie nowego zamowienia
INSERT INTO Zamowienia(zam_numer, zam_data, kl_id)
VALUES (@zam_numer, GETDATE() , @kl_id)
-- Zwrocenie numeru zamowienia
RETURN @zam_numer;