from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import imageio
import pandas as pd

# Load your predicted data
df = pd.read_csv('predicted_bloom_dates.csv')

# Latitude and longitude for Sapporo, Japan
lat, lon = 43.06, 141.35

# Your years and bloom_dates data
years = df['Year'].tolist()
bloom_dates = df['BloomDate'].tolist()

# Loop over each year and bloom date
for year, bloom_date in zip(years, bloom_dates):
    # Create a new figure
    plt.figure()

    # Create a basemap
    m = Basemap(projection='mill',llcrnrlat=20,urcrnrlat=50,\
                llcrnrlon=120,urcrnrlon=160,resolution='c')
    m.drawcoastlines()
    m.fillcontinents(color='coral',lake_color='aqua')
    m.drawmapboundary(fill_color='aqua')

    # Add a point for the bloom date
    x, y = m(lon, lat)
    m.plot(x, y, 'bo', markersize=24)

    # Add a title
    plt.title(f"Bloom date for {year}: {bloom_date}")

    # Save the figure
    plt.savefig(f"map_{year}.png")

# Create a list of filenames
filenames = [f"map_{year}.png" for year in years]

# Create a gif from the images
images = [imageio.imread(filename) for filename in filenames]
imageio.mimsave('output.gif', images, duration=0.5)