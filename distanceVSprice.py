import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#getting datasets
data = pd.read_csv('amsterdam_listings.csv')
places=pd.read_csv('tourism_listings.csv') 
x = data['longitude']
y = data['latitude']
distance = []
#choosing location names
lat=places['latitude']
long=places['longtitude']
place=places['place']
length=len(lat)
i=1
while(i<length):
    print(i,')',place[i],sep="")
    i+=1
loc=int(input(print("Choose a place: ")))
pointlong=long[loc]
pointlat=lat[loc]

#distance vs price plots
#finding distance using latitude and longitudes valuesand apending distance and price to distance[]
for a,b,c in zip(x,y,data['price']):
    if(c<300 and (sqrt((pointlong-a)*(pointlong-a) + 
    (pointlat-b)*(pointlat-b)))*(0.000001107042925553966/0.00000001)<20):
        distance.append([(sqrt((pointlong-a)*(pointlong-a) + 
    (pointlat-b)*(pointlat-b)))*(0.000001107042925553966/0.00000001),c])

# Plot using DataFrame data
# Scatter Plot
ax1 = plt.subplot(121)
ax1.set_xlabel('Distance (km)')
ax1.set_ylabel('Price (€)')
ax1 = plt.scatter(DistancePrice['Distance (km)'],DistancePrice['Price (€)'],color='Red') 
plt.title(place[loc])



