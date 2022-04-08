# Instrukcja tworzy klucz glowny oparty na kolumnie 'dost_id' ale z uzyciem skladni 'CONSTRAIN'
# Skladnie mozna zastosowac w poleceniach 'CREATE TABLE' i 'ALTER TABLE'

ALTER TABLE Dostawy
ADD CONSTRAINT PRIMARY KEY (dost_id)