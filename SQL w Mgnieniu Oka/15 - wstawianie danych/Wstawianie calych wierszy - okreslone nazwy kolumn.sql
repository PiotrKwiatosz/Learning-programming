# Bezpieczniejsze jest stosowanie ponizszej instrukcji, gdzie jawnie zostaly okreslone nazwy kolumn gdzie maja byc wstawione wartosci

INSERT INTO Klienci(kl_id,
	kl_nazwa,
    kl_adres,
    kl_miasto,
    kl_woj,
    kl_kod,
    kl_kraj,
    kl_kontakt,
    kl_email)
VALUES ('1000000006',
	'Zabawkolandia',
    'Miodowa 12',
    'Katowice',
    'SLK',
    '41-200',
    'Polska',
    NULL,
    NULL);