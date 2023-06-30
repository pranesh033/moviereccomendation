#!/usr/bin/env python
# coding: utf-8

# In[28]:


try: 
    import pandas as pd
    import numpy as np
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except:
    print("Some Modules are Missing")

class get_data:
    def __init__(self,path):
        self.data = pd.read_csv(path).drop(["Unnamed: 0"],axis=1)
        vectorizer = CountVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform(self.data["tag_2"]).toarray()
        self.similarity = cosine_similarity(vectors)
        
    def recommend_movies(self,movie):
        try:
            self.entered_movie = movie
            index = self.data[self.data['Title'] == self.entered_movie].index[0]
            distances = sorted(list(enumerate(self.similarity[index])),reverse=True,key = lambda x: x[1])
            self.recommended_movies = []
            for i in distances[1:6]:
                self.recommended_movies.append(self.data.iloc[i[0]].Title)
            return self.recommended_movies
        except:
            print("Sorry can't find Entered Movie")

