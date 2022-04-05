# Procedura 'ZliczanieListyMailingowej' dla systemu Microsoft SQL Server

CREATE PROCEDURE ZliczanieListyMailingowej
AS
DECLARE @cnt INTEGER
SELECT @cnt = COUNT (*)
FROM Klienci
WHERE NOT kl_email IS NULL;
RETURN @cnt;