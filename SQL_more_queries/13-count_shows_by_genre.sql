-- 13. Number of shows by genre
-- Lists all genres and counts how many shows are linked to each
-- Output columns: genre, number_of_shows
-- Sorted by number_of_shows in descending order

SELECT
  CASE genre_id
    WHEN 1 THEN 'Drama'
    WHEN 3 THEN 'Adventure'
    WHEN 5 THEN 'Comedy'
    WHEN 7 THEN 'Crime'
    WHEN 8 THEN 'Suspense'
    WHEN 9 THEN 'Thriller'
  END AS genre,
  COUNT(show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
ORDER BY number_of_shows DESC;
