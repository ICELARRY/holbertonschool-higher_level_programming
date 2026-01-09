-- 14. My genres
-- Lists all genres linked to the show Dexter
-- Output column: name
-- Sorted by genre name in ascending order

SELECT tg.name
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN tv_shows ts ON ts.id = tsg.show_id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
