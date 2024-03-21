import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("../movies.json").read_text())

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO movies VALUES(?, ?, ?)"
    [conn.execute(command, tuple(movie.values())) for movie in movies]
    conn.commit()


with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM movies"
    [print(row) for row in conn.execute(command)]
    # movies = conn.execute(command).fetchall()
    # print(movies)
    conn.commit()
