import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# step 1 data loading#
df= pd.read_csv(r"C:\Users\pramo\movies_boxoffice_data.csv")
print(df)

# step 2 data cleaning#
print(df.info)
print(df.head())

#step 3 data manipulating usinng python tools#
#which movie hit or flop#
print(df['budget_millions'])
df['status']=np.where(df['budget_millions']>150,'hit','flop')
print(df['status'])
print(df.drop('movie_id'))
print(df.head())
df['imdb_rating']=df['imdb_rating'].fillna(df['imdb_rating'].mean())

#which movie has the highest rating#
highest_rating=df['imdb_rating'].max()
best_movie=df.loc[df['imdb_rating'].idxmax(),"movie_name"]
print("highest rated movie :"+ str(best_movie) +"(rating:"+str(highest_rating)+")")

#what are the top 5 or which is the topest movie#
top_5=df.nlargest(5,'imdb_rating')
print(top_5[['movie_name','imdb_rating']])

#what is the avrage movie rating#
avg_rating=df['imdb_rating'].mean()
print("average movie rating:",round(avg_rating,2))

#how many movies have rating above 8#
mrating_above8=len(df[df['imdb_rating']>8])
print("movies with rating above 8:",mrating_above8)

#step 4 data visualization#
#data visualization using matplotlib#
top_5=df.nlargest(5,'imdb_rating')
plt.bar(top_5['movie_name'],top_5['imdb_rating'],color='skyblue')
plt.xlabel('movie name')
plt.ylabel('imdb rating')
plt.title('top 5 highest rated movies')
plt.show()

#movie hit or flop using pie chart#
status_count=df['status'].value_counts()
plt.pie(status_count,labels=status_count.index,autopct='%1.1f%%',colors=['lightgreen','red'])
plt.title('hit vs flop movies percentage')
plt.show()