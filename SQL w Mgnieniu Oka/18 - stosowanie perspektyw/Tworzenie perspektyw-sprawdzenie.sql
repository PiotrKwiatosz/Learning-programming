# Sprawdzenie perspektywe 'ProduktyKlientow' dla klientow ktorzy zamowili 'RGAN01'

SELECT kl_nazwa, kl_kontakt
FROM ProduktyKlientow
WHERE prod_id = 'RGAN01';