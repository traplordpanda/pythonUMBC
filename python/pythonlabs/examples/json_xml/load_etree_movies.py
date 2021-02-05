#!/usr/bin/env python3
import xml.etree.ElementTree as ET

root = ET.parse("movies.xml").getroot()

for movie in root.iter("movie"):
    movie_id = movie.attrib["id"]
    movie_title = movie.find("title").text
    print(f"{movie_id} : {movie_title}", end="")

    movie_rating = movie.find("rating").text
    if movie_rating:
        print(f" : {movie_rating}", end="")

    liked_it = movie.find("liked_it").text
    if float(liked_it) > 0.9:
        print(f" : {liked_it}", end="")
    else:
        print(" : rotten", end="")

    print()
