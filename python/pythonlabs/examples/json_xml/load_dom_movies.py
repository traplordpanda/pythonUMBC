#!/usr/bin/env python3
from xml.dom import minidom

doc = minidom.parse("movies.xml")

movies = doc.getElementsByTagName("movie")
for movie in movies:
    movie_id = movie.getAttribute('id')
    movie_title = movie.getElementsByTagName("title")[0].childNodes[0].data
    print(f"{movie_id} : {movie_title}", end="")
    movie_rating = movie.getElementsByTagName("rating")[0]
    if movie_rating.hasChildNodes():
        print(f" : {movie_rating.childNodes[0].data}", end="")

    liked_it = movie.getElementsByTagName("liked_it")[0].childNodes[0].data
    if float(liked_it) > 0.9:
        print(f" : {liked_it}", end="")
    else:
        print(" : rotten", end="")

    print()
