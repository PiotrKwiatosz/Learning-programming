# Wywolanie procedury skladowej 'ZliczanieListyMailingowej' 
# Dziala on TYLKO w systemu Microsoft SQL Server

DECLARE @ZwracanaWartosc INT
EXECUTE @ ZwracanaWartosc=ZliczanieListyMailingowej;
SELECT @ZwracanaWartosc;