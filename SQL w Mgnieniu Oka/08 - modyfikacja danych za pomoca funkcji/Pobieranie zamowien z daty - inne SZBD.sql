# Funkcja pobierajaca wszystkie zamowienia z roku 2020

# Dla SQL Server

SELECT zam_numer
FROM Zamowienia
WHERE DATEPART(yy, zam_data) = 2020;

# Dla PostrageSQL

SELECT zam_numer
FROM Zamowienia
WHERE DATE_PART('uear', zam_data) = 2020;

# Dla Oracle

SELECT zam_numer
FROM Zamowienia
WHERE EXTRACT(year FROM zam_data) = 2020;

# Dla SQLite

SELECT zam_numer
FROM Zamowienia
WHERE strftime('%Y', zam_data) = 2020;