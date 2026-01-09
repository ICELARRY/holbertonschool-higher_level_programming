-- 15. Only Comedy
-- Lists all TV shows that are in the Comedy genre
-- Output column: title
-- Sorted by title in ascending order

SELECT ts.title
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tg.id = tsg.genre_id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
