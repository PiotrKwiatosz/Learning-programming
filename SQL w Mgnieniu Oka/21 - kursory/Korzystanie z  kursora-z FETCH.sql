# W tym przykladzie polecenie 'FETCH' pobiera aktualny wiersz (domuslnie wiersz 1) do zmiennej 'KlRekord'

DECLARE TYPE Kursor IS REF CURSOR
	RETURN Klienci %ROWTYPE;
DECLARE KlRekord Klienci%ROWTYPE
BEGIN
	OPEN Kursor
    FETCH Kursor INTO KlRekord;
    CLOSE Kursor;
END;