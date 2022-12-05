-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT s.title, t.genre_id
FROM tv_shows AS s
    INNER JOIN tv_show_genre AS t
    ON s.id = t.show_id
ORDER BY s.title, t.genre_id;
