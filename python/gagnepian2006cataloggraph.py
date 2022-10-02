import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import cv2
import numpy as np

## Latitudinal, Longitudinal Data

url = 'https://github.com/Jane2210/selenes-compass/blob/main/index/gagnepian_2006_catalog.csv?raw=true'
df = pd.read_csv(url, index_col=0)

geometry = [Point(xy) for xy in zip(df['Long'], df['Lat'])]
gdf = GeoDataFrame(df, geometry=geometry)   

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


gdf.plot(marker='o', color='blue', markersize=50, ax=world.boundary.plot(figsize=(15, 15), edgecolor='white'));
