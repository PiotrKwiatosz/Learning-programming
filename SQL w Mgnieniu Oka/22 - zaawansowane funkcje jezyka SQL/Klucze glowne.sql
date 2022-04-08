# Do definicji tabelki zostalo dodane slowo kluczowe 'PRIMARY KEY' przez co 'dost_id' stalo sie kluczem glownym tabeli

CREATE TABLE Dostawcy
(
	dost_id		CHAR(10)	NOT NULL PRIMARY KEY,
    dost_nazwa	CHAR(50)	NOT NULL,
    dost_adres	CHAR(50)	NULL,
    dost_miasto	CHAR(50)	NULL,
    dost_woj	CHAR (5)	NULL,
    dost_kod	CHAR(10)	NULL,
    dost_kraj	CHAR(50)	NULL
);