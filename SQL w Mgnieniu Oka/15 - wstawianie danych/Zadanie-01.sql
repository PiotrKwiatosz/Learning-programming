# Uzywajac instrukcji INSERT dodaje swoje dane do tabeli Klienci
# Podaje dodawane kolumny i uzywam tych ktore potrzebuje

INSERT INTO Klienci(kl_id,
		kl_nazwa,
        kl_adres,
        kl_miasto,
        kl_woj,
        kl_kod,
        kl_kraj,
        kl_email)
VALUES('1000000042',
	'SQLowanie'
    'Sasankowa 6'
    'Katowice'
    'SLK',
    '48-330',
    'Polska',
    'pkwiatosz@sql.com');