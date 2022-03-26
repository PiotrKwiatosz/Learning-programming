# Instrukcja INSERT wypelnia wszystkie kolumny wiersza, ale dokonuje tego w innej kolejnosci

INSERT INTO Klienci(kl_id,
		kl_kontakt,
        kl_email,
        kl_nazwa,
        kl_adres,
        kl_miasto,
        kl_woj,
        kl_kod,
        kl_kraj)
	VALUES('1000000006',
		NULL,
        NULL,
        'Zabawkolandia',
        'Miodowa',
        'Katowice',
        'SLK',
        '41-200',
        'Polska');