from flask import render_template, request, Flask, redirect, url_for
import os
import numpy as np
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import poster_url
import recommendation_system
import os
import image_url

app = Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def home():
    return render_template("n.html")
@app.route("/recommend" , methods = ["POST","GET"])
def get_image():
    if request.method == "POST":
        entered_movie = movies()
        path=os.getcwd()+os.path.sep+"meta_movies.csv"
        recommender = recommendation_system.get_data(path=path)
        recommended_movies = recommender.recommend_movies(movie=entered_movie)
        movie_posters = []
        for re_movie in recommended_movies:
            links = image_url.google_image_url(n=1,query=re_movie+" tamil movie poster")
            movie_posters.append(links.get_imageurl())
        return render_template("index2.html",
        entered_movie = entered_movie,
        movie1 = recommended_movies[0],
        movie2 = recommended_movies[1],
        movie3 =recommended_movies[2]
        ,movie4 = recommended_movies[3],
        movie5 = recommended_movies[4],
        link1 = movie_posters[0],
        link2 = movie_posters[1],
        link3 = movie_posters[2],
        link4 = movie_posters[3],
        link5 = movie_posters[4])
def movies():
    movie = str(request.form.get("movie"))
    return movie


    
if __name__ == "__main__" :
    app.run(debug = True)

