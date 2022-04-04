# Tworzenie perspektywy filtrujacej klientow ktorzy podali swoj adre email

CREATE VIEW AdresyEmailKlientow AS
SELECT kl_id, kl_nazwa, kl_email
FROM Klienci
WHERE kl_email IS NOT NULL;