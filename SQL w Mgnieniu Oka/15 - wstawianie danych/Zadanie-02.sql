# Kopia zapasowa tabek Zamowienie i ElementyZamowienia

CREATE TABLE KopiaZamowienia AS SELECT * FROM Zamowienia;
CREATE TABLE KopiaElementyZamowienia AS SELECT * FROM ElementyZamowienia;