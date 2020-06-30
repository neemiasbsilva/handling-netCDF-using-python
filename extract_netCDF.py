import argparse
from netCDF4 import Dataset
import numpy as np

parser = argparse.ArgumentParser(description="Extracting netCDF files into csv")
parser.add_argument("-file_name", action="store", required=True,
                    help="Name of netCDF file", dest="file_name")

arguments = parser.parse_args()
file_name = arguments.file_name

dataset = Dataset(filename=file_name)

# display the names of the variables
print(dataset.variables.keys())

# Accessing the variables
longitude = dataset.variables['lon']
latitude = dataset.variables['lat']
time = dataset.variables['time']
tave = dataset.variables['tave']
rstn = dataset.variables['rstn']

# print("_"*80)
# print("\tLongitude")
# print(longitude)
# print("_"*80)
# print("\tLatitude")
# print(latitude)
print("_" * 80)
print("\tTime")
print(time)
print("_" * 80)
# print("\tDaily mean temperature")
# print(tave)
# print("_"*80)
# print("\tRation")
# print(rstn)
# print("_"*80)

# dimensions variables
print("Longitude: {}".format(longitude.dimensions))
print("Latitude: {}".format(latitude.dimensions))
print("Time: {}".format(time.dimensions))
print("Temperature: {}".format(tave.dimensions))
print("Ratio: {}".format(rstn.dimensions))

# Accessing data from the variables
longitude_data = dataset.variables['lon'][:]
latitude_data = dataset.variables['lat'][:]
time_data = dataset.variables['time'][:]
tave_data = dataset.variables['tave'][:]
rstn_data = dataset.variables['rstn'][:]


print("_"*80)
print("Longitude length: {}\n Longitude[0]: {}".format(
    len(longitude_data), longitude_data[0]))

print("Latitude length: {}\n Latitude[0]: {}".format(
    len(latitude_data), latitude_data[0]))

print("Time length: {}\n Time[0]: {}".format(
    len(time_data), time_data[0]))

print("Temperature length: {}\n Temperature[0]: {}".format(
    len(tave_data), tave_data[0]))

print("Ratio length: {}\n Ratio[0]: {}".format(
    len(rstn_data), rstn_data[0]))
print("_"*80)

