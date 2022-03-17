# Zwracanie identyfikatorow klientow wraz z sumaryczna wartoscia ich zamowien

SELECT kl_id,
        (SELECT SUM(cena_elem*ilosc)
        FROM ElementyZamowienia
        WHERE Zamowienia.zam_numer = ElementyZamowienia.zam_numer) AS wartosc_zam
FROM Zamowienia
ORDER BY wartosc_zam DESC;