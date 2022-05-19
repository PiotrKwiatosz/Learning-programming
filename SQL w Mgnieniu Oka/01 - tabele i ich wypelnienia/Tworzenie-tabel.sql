--------------------------------------------------
## Skrypt tworzenia tabel dla bazy danych MySQL.
--------------------------------------------------


---------------------------
-- Tworzenie tabeli Klienci
---------------------------
CREATE TABLE Klienci
(
  kl_id      char(10)  NOT NULL ,
  kl_nazwa   char(50)  NOT NULL ,
  kl_adres   char(50)  ,
  kl_miasto  char(50)  ,
  kl_woj     char(5)   ,
  kl_kod     char(10)  ,
  kl_kraj    char(50)  ,
  kl_kontakt char(50)  ,
  kl_email   char(255) 
);

--------------------------------------
-- Tworzenie tabeli ElementyZamowienia
--------------------------------------
CREATE TABLE ElementyZamowienia
(
  zam_numer  	int          NOT NULL ,
  zam_element 	int          NOT NULL ,
  prod_id    	char(10)    NOT NULL ,
  ilosc 		int          NOT NULL ,
  cena_elem 	decimal(8,2) NOT NULL 
);

------------------------------
-- Tworzenie tabeli Zamowienia
------------------------------
CREATE TABLE Zamowienia
(
  zam_numer  int       NOT NULL ,
  zam_data	 datetime  NOT NULL ,
  kl_id      char(10) NOT NULL 
);

----------------------------
-- Tworzenie tabeli Produkty
----------------------------
CREATE TABLE Produkty
(
  prod_id     char(10)      NOT NULL ,
  dost_id     char(10)      NOT NULL ,
  prod_nazwa  char(255)     NOT NULL ,
  prod_cena   decimal(8,2)   NOT NULL ,
  prod_opis   text      NULL 
);

----------------------------
-- Tworzenie tabeli Dostawcy
----------------------------
CREATE TABLE Dostawcy
(
  dost_id      char(10) NOT NULL ,
  dost_nazwa   char(50) NOT NULL ,
  dost_adres   char(50) NULL ,
  dost_miasto  char(50) NULL ,
  dost_woj     char(5)  NULL ,
  dost_kod     char(10) NULL ,
  dost_kraj    char(50) NULL 
);

-------------------------------
-- Definiowanie kluczy głównych
-------------------------------
ALTER TABLE Klienci ADD PRIMARY KEY (kl_id);
ALTER TABLE ElementyZamowienia ADD PRIMARY KEY (zam_numer, zam_element);
ALTER TABLE Zamowienia ADD PRIMARY KEY (zam_numer);
ALTER TABLE Produkty ADD PRIMARY KEY (prod_id);
ALTER TABLE Dostawcy ADD PRIMARY KEY (dost_id);

-----------------------------
-- Definiowanie kluczy obcych
-----------------------------
ALTER TABLE ElementyZamowienia ADD CONSTRAINT FK_OrIt_Or FOREIGN KEY (zam_numer) REFERENCES Zamowienia (zam_numer);
ALTER TABLE ElementyZamowienia ADD CONSTRAINT FK_OrIt_Pr FOREIGN KEY (prod_id) REFERENCES Produkty (prod_id);
ALTER TABLE Zamowienia ADD CONSTRAINT FK_Or_Cu FOREIGN KEY (kl_id) REFERENCES Klienci (kl_id);
ALTER TABLE Produkty ADD CONSTRAINT FK_Pr_Ve FOREIGN KEY (dost_id) REFERENCES Dostawcy (dost_id);
