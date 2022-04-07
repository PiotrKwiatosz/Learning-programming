# Zdefiniowane zmienne dla kazdej z pobieranych kolumn, 'FETCH' pobiera wiersze i zapisuje, petla 'WHILE' umozliwia pobranie wszystkich wierszy a konstrukcja 'WHILE @@FETCH_STATUS = 0' umozliwia opuszczenie petli po pobraniu.

# Dla SQL Server

DECLARE @kl_id CHAR(10),
		@kl_nazwa CHAR(50);
        @kl_adres CHAR(50);
        @kl_miasto CHAR(50);
        @kl_woj CHAR(5);
        @kl_kod CHAR(10);
        @kl_kraj CHAR(50);
        @kl_kontakt CHAR(50);
        @kl_email CHAR(255)
OPEN Kursor
FETCH NEXT FROM Kursor
	INTO @kl_id, @kl_nazwa, @kl_adres, @kl_miasto, @kl_wojm @kl_kod, @kl_kraj, @kl_kontakt, @kl_email
	...
WHILE @@FETRCH_STATUS = 0
BEGIN

FETCH NEXT FROM Kursor
	INTO @kl_id, @kl_nazwa, @kl_adres, @kl_miasto, @kl_wojm @kl_kod, @kl_kraj, @kl_kontakt, @kl_email
    ...
END
CLOSE Kursor