import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import shapefile as shp
from shapely.geometry import Point
import os
sns.set_style('whitegrid')

fp = "codeforproject/india-polygon.shp"
map_df = gpd.read_file(fp) 
map_df_copy = gpd.read_file(fp)

df = pd.read_csv('codeforproject/crimeplot.csv')
df_copy = pd.read_csv('codeforproject/crimeplot.csv')  # making a copy of dataframe

pd.set_option('display.max_columns', None)

fp = 'codeforproject/india-polygon.shp'
map_df = gpd.read_file(fp)                          # Reads the shape file of India for plotting purpose
map_df_copy = gpd.read_file(fp)

cr_df = df[df.Count=="Count"]

cnt_df = cr_df["Count"].value_counts()   # This gives the number of landslides that took place in every state over the years

fp = 'codeforproject/india-polygon.shp'
map_df = gpd.read_file(fp)                          # Reads the shape file of India for plotting purpose
map_df_copy = gpd.read_file(fp)

State_df=df
#Merging the data
merged = map_df.set_index('st_nm').join(State_df.set_index('STATE'))
merged['Count'] = merged['Count'].replace(np.nan, 0)

#Create figure and axes for Matplotlib and set the title
fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('Crime Density Prediction', fontdict={'fontsize': '20', 'fontweight' : '10'})

# Plot the figure
merged.plot(column='Count',cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0', \
            legend=True,markersize=[39.739192, -104.990337], legend_kwds={'label': "Crime-Sentiment value"})

plt.savefig('imgplot.png')

command = 'python codeforproject/gui.py'
os.system(command)