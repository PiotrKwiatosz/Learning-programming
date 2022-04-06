# Pelny przyklad wstawiania zamowienia do bazy danych. Zawiera 4 instrukcji 'INSERT', punkt kontrony zostal zdefiniowany zaraz za 1 instrukcja 'INSERT'
# W celu sprawdzenia poprawnosci wykonania instrukcji SQLowej korzysta sie ze zmiennej globalneg '@@ERROR'

# Dla SQL Server

BEGIN TRANSACTION
INSERT INTO Klienci(kl_id, kl_nazwa)
VALUES ('1000000010', 'Imperium zabawek')
SAVE TRANSATION PoczZamowienia;
INSERT INTO Zamowienia(zam_numer, zam_data, kl_id)
VALUES (20100, '2020/12/1', '1000000010');
IF @@ERROR <> 0 ROLLBACK TRANSACTION PoczZamowienia;
INSERT INTO ElementyZamowienia(zam_numer, zam_element, prod_id, ilosc, cena_elem);
VALUES (20100, 1, 'BR01', 100, 19.99);
IF @@ERROR <> 0 ROLLBACK TRANSACTION PoczZamowienia;
INSERT INTO ElementyZamowienia(zam_numer, zam_element, prod_id, ilosc, cena_elem);
VALUES (20100, 2, 'BR03' 100, 44.99);
IF @@ERROR <> ) ROLLBACK TRANSACTION PoczZamowienia;
COMMIT TRANSACTION