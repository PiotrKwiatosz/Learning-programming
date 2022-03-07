# Funkcja SOUNDEX - znajdowanie rzeczy na podstawie ich wymowy i brzmienia

SELECT kl_nazwa, kl_kontakt
FROM Klienci
WHERE SOUNDEX(kl_kontakt) = SOUNDEX('Michael Znany');