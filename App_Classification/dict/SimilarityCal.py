import sys
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

new_app_desc = sys.argv[1] 

Edu_Dict = open("EducationAppDesc_p.txt","r").read()
Ent_Dict = open("EntertainmentAppDesc_p.txt","r").read()
Food_Dict = open("FoodAppDesc_p.txt","r").read()
Game_Dict = open("GameAppDesc_p.txt","r").read()
Music_Dict = open("MusicAppDesc_p.txt","r").read()
Busi_Dict = open("BusinessAppDesc_p.txt","r").read()

new_app_desc = open(new_app_desc,"r").read()

#Cosine Similarity
tfidf_vectorizer=TfidfVectorizer()

Edu_doc = (new_app_desc,Edu_Dict)
Ent_doc = (new_app_desc,Ent_Dict)
Food_doc=(new_app_desc,Food_Dict)
Game_doc=(new_app_desc,Game_Dict)
Music_doc=(new_app_desc,Music_Dict)
Busi_doc=(new_app_desc,Busi_Dict)

Edu_tfidf=tfidf_vectorizer.fit_transform(Edu_doc)
Ent_tfidf=tfidf_vectorizer.fit_transform(Ent_doc)
Food_tfidf=tfidf_vectorizer.fit_transform(Food_doc)
Game_tfidf=tfidf_vectorizer.fit_transform(Game_doc)
Music_tfidf=tfidf_vectorizer.fit_transform(Music_doc)
Busi_tfidf=tfidf_vectorizer.fit_transform(Busi_doc)

Edu=((Edu_tfidf*Edu_tfidf.T).A)[0,1]
Ent=((Ent_tfidf*Ent_tfidf.T).A)[0,1]
Food=((Food_tfidf*Food_tfidf.T).A)[0,1]
Game=((Game_tfidf*Game_tfidf.T).A)[0,1]
Music=((Music_tfidf*Music_tfidf.T).A)[0,1]
Bus= ((Busi_tfidf*Busi_tfidf.T).A)[0,1]



##print "Cosine Simiarity with Edu: " + str(((Edu_tfidf*Edu_tfidf.T).A)[0,1])
##print "Cosine Simiarity with Ent: " + str(((Ent_tfidf*Ent_tfidf.T).A)[0,1])
##print "Cosine Simiarity with Food: " + str(((Food_tfidf*Food_tfidf.T).A)[0,1])
##print "Cosine Simiarity with Game: " + str(((Game_tfidf*Game_tfidf.T).A)[0,1])
##print "Cosine Simiarity with Music: " + str(((Music_tfidf*Music_tfidf.T).A)[0,1])
##print "Cosine Simiarity with Business: " + str(((Busi_tfidf*Busi_tfidf.T).A)[0,1])

# Plotting the similarity measures with each dictionaries
objects = ('Edu', 'Ent', 'Food', 'Games', 'Music', 'Busi')
y_pos = np.arange(len(objects))
Similarity = [Edu,Ent,Food,Game,Music, Bus]
 
plt.bar(y_pos, Similarity, align='center', width = 0.5, alpha=0.25)
plt.xticks(y_pos, objects)
plt.ylabel('Similarity Measure')
plt.title('Affinity')
 
plt.show()

