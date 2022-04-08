# Instrukcja prezentuje wyzwalacz ktory konwertuje wartosci kolumny 'kl_woj' z tabeli 'Klienci' na wielkie litery we wszystkich operacjach INSERT i UPDATE

# Wersja dla SQL Server

CREATE TRIGGER klient_woj
ON Klienci
FOR INSERT, UPDATE
AS
UPDATE Klienci
SET kl_woj = Upper(kl_woj)
WHERE Klienci.kl_woj = inserted.kl_woj;