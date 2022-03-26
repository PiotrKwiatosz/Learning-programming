# Podawanie wartosci w INSERT tylko dla niektorych kolumn wiersza, tych ktore nie sa puste

INSERT INTO Klienci(kl_id,
	kl_nazwa,
    kl_adres,
    kl_miasto,
    kl_woj,
    kl_kod,
    kl_kraj)
VALUES('1000000006',
	'Zabawkolandia',
    'Miodowa',
    'Katowice',
    'SLK',
    '41-200',
    'Polska');