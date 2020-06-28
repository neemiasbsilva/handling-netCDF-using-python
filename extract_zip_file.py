import patoolib
import os


for zip_file in os.listdir(r"./"):
    if zip_file[-3:] == ".gz":
        patoolib.extract_archive(zip_file, outdir=r"./netCDF-temperature")

for extracted_file in os.listdir(r"./netCDF-temperature"):
    os.chdir(r"./netCDF-temperature")
    os.rename(extracted_file, extracted_file+".nc")
