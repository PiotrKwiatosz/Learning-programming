# Wstawianie nowej pozycji do tabeli 'Zamowienia'

# Wersja dla SQL Server

CREATE PROCEDURE NoweZamowienie @kl_id CHAR(10)
AS
-- Wstawienie nowego zamowienia
INSERT INTO Zamowienia(kl_id)
VALUES (@kl_id)
-- Zwrocenie numeru zamowienia
SELECT zam_numer = @@IDENTITY;