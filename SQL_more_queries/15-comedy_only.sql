-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_shows.title
    FROM tv_show_genres
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = "Comedy"
    ORDER BY tv_shows.title ASC