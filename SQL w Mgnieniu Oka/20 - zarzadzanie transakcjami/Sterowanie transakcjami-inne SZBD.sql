# Wszystkie instrukcje miedzy 'BEGIN TRANSACTION' a 'COMMIT TRANSACTION' musza zostacj wykonane poprawnie w przeciwnym wypadku operacje nalezy anulowac

# '...' - jakis kod SQL


# Dla SQL Server

BEGIN TRANSACTION
...
COMMIT TRANSACTION

# Dla Oracle

SET TRANSACTION
...

# Dla PostrgeSQL

BEGIN
...