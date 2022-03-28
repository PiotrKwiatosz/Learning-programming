# Instrukcja tworzy tabele 'Dostawcy'
# Przyklad z mieszanka kolumn (NULL i NOT NULL-> domyslnie puste)

CREATE TABLE Dostawcy
(
	dost_id		CHAR(10)	NOT NULL,
    dost_nazwa	CHAR(50)	NOT NULL,
    dost_adres	CHAR(50)	,
    dost_miasto	CHAR(50)	,
    dost_woj	CHAR(5)		,
    dost_kod	CHAR(10)	,
    dost_kraj	CHAR(50)
);