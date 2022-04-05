# Procedura przyjmuje 1 parametr 'RozmiarListy' przekazuje on dane na zewnatrz (przez zastosowanie 'OUT')
# Sam kod procedury znajduje sie pomiedzy 'BEGIN' i 'END'. Pomiedzy nimi znajduje sie SELECT ktora pobiera klientow z adresami email

# Dla systemu Oracle

CREATE PROCEDURE ZliczanieListyMailingowej(
	RozmiarListy OUT NUMBER
)
IS
l_wierszy INTEGER;
BEGIN
	SELECT COUNT (*) INTO l_wiersz
    FROM Klienci
    WHERE NOT kl_email IS NULL;
    RozmiarListy := l_wierszy;
END;