# -*- coding: utf-8 -*-
"""Indonesia Tourism Recommendation Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hEQMIYHX_sdKoMf9waUEMzn7WCtT6q-b

# Data Understanding

## Preparasi Modul
"""

!pip install -q kaggle
!pip install scikit-learn

"""## Data Loading"""

import zipfile, os
import numpy as np
import itertools
import cv2
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score, f1_score

from google.colab import files
files.upload()
!rm -r ~/.kaggle
!mkdir ~/.kaggle
!mv ./kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d aprabowo/indonesia-tourism-destination

zip_ref = zipfile.ZipFile('indonesia-tourism-destination.zip', 'r')
zip_ref.extractall('/content')
zip_ref.close()

rating = pd.read_csv('/content/tourism_rating.csv')
id = pd.read_csv('/content/tourism_with_id.csv')[['Place_Id',	'Place_Name',	'Description',	'Category',	'City',	'Price',	'Rating',	'Time_Minutes',	'Coordinate',	'Lat',	'Long']]
user = pd.read_csv('/content/user.csv')

"""## Univariate Exploratory Data Analysis

### Rating Data
"""

rating.head()

rating.info()

"""### id Data"""

id.head()

id.info()

"""### User Data"""

user.head()

user.info()

"""## Visualisasi Data

### Penggabungan data
"""

tourism_all = np.concatenate((
    id.Place_Id.unique(),
    rating.Place_Id.unique()
))

tourism_all = np.sort(np.unique(tourism_all))
len(tourism_all)

all_tourism_rate = rating
all_tourism_rate

all_tourism = pd.merge(all_tourism_rate, id[['Place_Id',	'Place_Name', 'City','Category']], on='Place_Id', how='left')
all_tourism.head()

"""### Grafik Category"""

category_counts = all_tourism['Category'].value_counts()

plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Jumlah Setiap Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

"""### Grafik City"""

city_counts = all_tourism['City'].value_counts()

plt.figure(figsize=(10, 6))
city_counts.plot(kind='bar', color='salmon')
plt.title('Jumlah setiap city')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

"""### Grafik Rating"""

rating_counts = all_tourism['Place_Ratings'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
rating_counts.plot(kind='bar', color='lightgreen')
plt.title('Jumlah setiap Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

"""# Data Preparation

## Missing Value
"""

all_tourism.isnull().sum()

"""## Duplicate"""

df_tourism = all_tourism.drop_duplicates('Place_Id')
df_tourism.head()

"""## Konversi Menjadi list"""

user_id = df_tourism['User_Id'].tolist()
place_id = df_tourism['Place_Id'].tolist()
place_ratings = df_tourism['Place_Ratings'].tolist()
place_name = df_tourism['Place_Name'].tolist()
city = df_tourism['City'].tolist()
category = df_tourism['Category'].tolist()

df = pd.DataFrame({
    'user_id': user_id,
    'place_id': place_id,
    'place_ratings': place_ratings,
    'place_name': place_name,
    'city': city,
    'category': category
})
df.head()

"""## TF-IDF Vectorizer"""

tf = TfidfVectorizer()

tf.fit(df['category'])

tf.get_feature_names_out()

tfidf_matrix = tf.fit_transform(df['category'])

tfidf_matrix.shape

tfidf_matrix.todense()

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=df.place_name
).sample(10, axis=1).sample(10, axis=0)

"""# Modeling and Result (Content Based Filtering)

## Cosine Similarity
"""

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

cosine_sim_df = pd.DataFrame(cosine_sim, index=df['place_name'], columns=df['place_name'])
print('Shape:', cosine_sim_df.shape)

cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""## Recommendation"""

def tourism_recommendations(place_name, similarity_data=cosine_sim_df, items=df[['place_name', 'category', 'city']], k=10):
    index = similarity_data.loc[:, place_name].to_numpy().argpartition(range(-1, -k, -1))

    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    closest = closest.drop(place_name, errors='ignore')

    recommendations = pd.DataFrame(closest).merge(items).head(k)

    print(f"Apabila pengguna menyukai '{place_name}', 10 tempat berikut ini juga mungkin akan disukai: \n")
    return pd.DataFrame(closest).merge(items).head(k)

"""# Evaluation

## Top-N Recommendation (Candi Sewu)
"""

tourism_recommendations("Candi Sewu")

"""## Top-N Recommendation (NuArt Sclupture Park)"""

tourism_recommendations("NuArt Sculpture Park")

"""## Top-N Recommendation (Pantai Marina)"""

tourism_recommendations("Pantai Marina")