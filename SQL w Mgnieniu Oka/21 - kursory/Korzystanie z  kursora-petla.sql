# W tym przykladzie polecenie 'FETCH' pobiera aktualny wiersz (domuslnie wiersz 1) do zmiennej 'KlRekord'
# Pobieranie w petli

DECLARE TYPE Kursor IS REF CURSOR
	RETURN Klienci %ROWTYPE;
DECLARE KlRekord Klienci%ROWTYPE
BEGIN
	OPEN Kursor
    LOOP
    FETCH Kursor INTO KlRekord;
    EXIT WHEN Kursor%NOTFOUND;
    ...
    END LOOP;
    CLOSE Kursor;
END;