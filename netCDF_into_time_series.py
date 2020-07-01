import argparse
from netCDF4 import Dataset
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(description="Extracting netCDF files into csv")
parser.add_argument("-file_name", action="store", required=True,
                    help="Name of netCDF file", dest="file_name")
parser.add_argument("-csv_path", action="store", required=True,
                    help="Name of csv File to Save", dest="csv_path")
parser.add_argument("-specie_latitude", action="store", required=True,
                    help="The occurrence of the specie", dest="specie_latitude")
parser.add_argument("-specie_longitude", action="store", required=True,
                    help="The occurrence of the specie", dest="specie_longitude")

arguments = parser.parse_args()
file_name = arguments.file_name
csv_path = arguments.csv_path


# Reading the netCDF file
dataset = Dataset(filename=file_name)

# display the names of the variables
print(dataset.variables.keys())

# Accessing the variables
longitude = dataset.variables['lon']
latitude = dataset.variables['lat']
time = dataset.variables['time']
temperature = dataset.variables['tave']
rstn = dataset.variables['rstn']

# Accessing data from the variables
longitude_data = dataset.variables['lon'][:]
latitude_data = dataset.variables['lat'][:]
time_data = dataset.variables['time'][:]
temperature_data = dataset.variables['tave'][:]
rstn_data = dataset.variables['rstn'][:]

# Storing the lat and lon of alien-flora
alien_flora_lat = float(arguments.specie_latitude)
alien_flora_lon = float(arguments.specie_longitude)

# Squared difference of lat and long

sq_diff_lat = (latitude_data - alien_flora_lat) ** 2
sq_diff_lon = (longitude_data - alien_flora_lon) ** 2

# Identifying the min value for lat and lon
min_index_lat = sq_diff_lat.argmin()
min_index_lon = sq_diff_lon.argmin()

# Creating an empty data frame
starting_date = time.units[14:24]
ending_date = time.units[14:18] + "-12-31"
date_range = pd.date_range(start=starting_date, end=ending_date)
df = pd.DataFrame(0, columns=["Temperature"], index=date_range)

dt = np.arange(0, time.size)

for i in dt:
    df.iloc[i] = temperature_data[i, min_index_lat, min_index_lon]

df.to_csv(csv_path)
