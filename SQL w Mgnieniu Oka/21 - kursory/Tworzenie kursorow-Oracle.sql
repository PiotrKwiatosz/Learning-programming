# Utworzenie kursora ktory pobiera dane wszystkich klientow ktorzy nie maja adresu email

# Polecenie dla Oracle i PostgreSQL

DECLARE CURSOR Kursor
IS
SELECT * FROM Klienci
WHERE kl_email IS NULL;