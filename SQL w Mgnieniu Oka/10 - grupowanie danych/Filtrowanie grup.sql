# Filtrowanie grup przy pomocy HAVING ktora przepuszcza tylko te ktore posiadaja min. 2 zamowienia

SELECT kl_id, COUNT(*) AS zamowienia
FROM Zamowienia
GROUP BY kl_id
HAVING COUNT(*) >= 2;