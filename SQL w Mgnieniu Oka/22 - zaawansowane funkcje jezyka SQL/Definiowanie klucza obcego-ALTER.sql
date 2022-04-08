# Instrukcja definiuje klucz obcy, za pomoca skladni 'CONSTRAINT' w poleceniu 'ALTER TABLE'

ALTER TABLE klienci
ADD CONSTRAINT
FOREIGN KEY (kl_id) REFERENCES Klienci (kl_id)