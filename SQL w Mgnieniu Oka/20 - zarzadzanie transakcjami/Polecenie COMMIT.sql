# Zamowienie '12345' jest calkowicie usuwane z bazy. Poniewaz wymaga uaktualnienia 'Zamowienia' i 'ElementyZamowienia'. Stosuje sie blok transakcji w celu wykonania obu polecen.
# Koncowe 'COMMIT' zapisuje zmiany tylko wtedy gdy nie wystapily zadne bledy

# Dla SQL Server

BEGIN TRANSACTION
DELETE ElementyZamowienia WHERE zam_numer = 12345
DELETE Zamowienia WHERE zam_numer 12345
COMMIT TRANSACTION


