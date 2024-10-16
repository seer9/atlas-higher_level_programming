-- lists all shows, and all genres linked to a show
SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.id = tv_genres.tv_show_id
ORDER BY tv_shows.title, tv_genres.name;