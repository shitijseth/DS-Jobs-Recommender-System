import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from itertools import combinations
import random
from sklearn.preprocessing import LabelEncoder
from  geopy.geocoders import Nominatim
from geopy.distance import geodesic
from sklearn.metrics.pairwise import cosine_similarity


#Jaccard similarity between advertisement skills and candidate skills
def skill_match_score(ad_skills, cand_skills):
  cand_skills, ad_skills = set(cand_skills), set(ad_skills)
  return len(cand_skills.intersection(ad_skills)) / len(cand_skills.union(ad_skills))

#Vectorize data
def vectorize(data):
    return [data['exp'], data['skills'], data['city']]

#Function to calculate cosine similarity
def cos_similarity_metric(cand, ad):
#Extract city and skill set data
    city1, city2 = cand[2], ad[2]
    skill1, skill2 = cand[1], ad[1]

#Calling API for location
    geolocator = Nominatim(user_agent =)

#Getting longitude and latitude for cities
    loc1 = geolocator.geocode(cand[2])
    loc2 = geolocator.geocode(ad[2])

    lonlat1 = (loc1.latitude,loc1.longitude)
    lonlat2 = (loc2.latitude,loc2.longitude)

#Calculating distance between the cities
    dis = geodesic(lonlat1, lonlat2).km #/ 4500

#Saving values in vectors for calculting similarity
    cand[2], ad[2] = 0, dis
    cand[1], ad[1] = 1, skill_match_score(skill1, skill2)

#Converting list(vector) to numpy array
    cand = np.asarray(cand)
    ad = np.asarray(ad)

#Calculting cosine similarity score
    score = cosine_similarity(cand.reshape(1,-1), ad.reshape(1,-1))

#Appending necessary data points (distance and skill score decoded)
    cand = np.append(cand, (skill1, city1))
    ad = np.append(ad, (skill2, city2))

#Deleting unnecessary data points (distance and skill score encoded)
    cand = np.delete(cand, [1,2])
    ad = np.delete(ad, [1,2])

#Adding score to ad data
    ad = np.append(ad, score)

    return ad.tolist()

#Funtion to match coach info se
def match_info(ad):
  for j in range(len(ads)):
    val = ad[0]
    if int(float(val)) == ads[j]['exp']:
      if ad[1] == ads[j]['skills']:
        if ad[2] == ads[j]['city']:
          print(ads[j])

#Function to print results
def print_results(n):
  print('Best jobs for you are')
  for k in range(n):
    match_info(ads_with_scores[k])

def recommend(ads, cand, n):
    ads_with_scores = []
#Looping through all coaches and calculating cosine similarity score
    for i in range(len(ads)):
      match = cos_similarity_metric(vectorize(cand), vectorize(ads[i]))
      ads_with_scores.append(match)

#Sorting in descinding order
    ads_with_scores.sort(key = lambda x: x[3], reverse = True)

    print_results(n)
