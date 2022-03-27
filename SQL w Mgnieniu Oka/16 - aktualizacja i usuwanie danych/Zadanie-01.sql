# Skroty nazw wojewodztw powinny skladac sie z wielkich liter

UPDATE Dostawcy
SET dost_woj = UPPER(dost_woj);

UPDATE Klienci
SET kl_woj = UPPER(kl_woj);