# Utworzenie kursora ktory pobiera dane wszystkich klientow ktorzy nie maja adresu email

# Polecenie dla DB2, MariaDB, SQL Server i MySQL

DECLARE Kursor CURSOR
FOR
SELECT * FROM Klienci
WHERE kl_email IS NULL;