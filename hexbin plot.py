import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

#reading values
data = pd.read_csv('amsterdam_listings.csv')
x = data['longitude']
y = data['latitude']
places=pd.read_csv('tourism_listings.csv')
lat=places['latitude']
long=places['longtitude']
place=places['place']
length=len(lat)
i=1
while(i<length):
    print(i,')',place[i],sep="")
    i+=1
loc1=int(input(("Choose first place:")))
loc2=int(input(("Choose second place:")))
loc3=int(input(("Choose third place:")))
pointlong1=long[loc1]
pointlat1=lat[loc1]
pointlong2=long[loc2]
pointlat2=lat[loc2]
pointlong3=long[loc3]
pointlat3=lat[loc3]

x05 = data['longitude'].quantile(.05)
x95 = data['longitude'].quantile(.95)
y05 = data['latitude'].quantile(.05)
y95 = data['latitude'].quantile(.95)

#color for plot
plt.hexbin(x,y, cmap = 'YlGnBu')
# Describe what the colorbar stands for
cbar = plt.colorbar()
cbar.set_label('Number of Listings')

#axis limit
ax = plt.subplot(111)
ax.set_xlim([x05,x95])
ax.set_ylim([y05,y95])

#Labels and Title
ax.set_title("Amsterdam listings density based on latitude and longitude")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Annotations for the median
ax.annotate('MD',color='red', xy = (x.quantile(.5),y.quantile(.5)))
ax.annotate(loc1,color='red', xy = (pointlong1,pointlat1))
ax.annotate(loc2,color='red', xy = (pointlong2,pointlat2))
ax.annotate(loc3,color='red', xy = (pointlong3,pointlat3))



    

    