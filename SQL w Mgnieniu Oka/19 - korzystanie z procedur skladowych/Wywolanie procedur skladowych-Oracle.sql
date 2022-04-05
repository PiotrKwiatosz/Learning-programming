# Wywołanie procedury składowej 'ZliczanieListMailinogowej' dla systemu Oracle

var ZwracanaWartosc NUMBER
EXEC ZliczanieListyMailingowej(:ZwracanaWartosc);
SELECT ZwracanaWartosc;