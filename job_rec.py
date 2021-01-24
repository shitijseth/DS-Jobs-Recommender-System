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
