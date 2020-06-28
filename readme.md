# Automating Mass Downloading netCDF File for use to GISS ( Goddard Institute for Space Studies) Software

## Network Common Data Form (netCDF) Overview

<p align="center"><img src="./images/netCDF-temperature.png" width="55%" height="45%">
</p><h6 align="center">Example of structure netCDF file.</h6>

NetCDF is a set of interfaces for array-oriented data access and self-describing, 
machine-independent data formats that support the creation, access, and sharing of array-oriented
scientific data.

## Repository Description

The goal of this repository is to researchers use with tool for 
get state-of-the-art daily precipitation dataset
[APHRODITE](https://www.chikyu.ac.jp/precip/english/). The APHRODITE, is
asian precipitation - highly - resolved observational data integration 
towards evaluation of water resources.

After you get the set of netCDF dataset you can use the NASA GISS to visualizing, 
analysing and extract time series of data.

## Getting Started

### Usage

To run the first step of this repository you need to set two arguments of
_run_mass_downloading.sh_ which are:

```
 -user_name name@user.com (example) \
 -password xxxxxxxx (example)
```

__Note:__ when you clone (or fork this) repository, you need create a folder
and nominate to __netCDF-temparature__.

After that, you can run the script using the terminal of you system operation:

```
 sh run_mass_downloading.sh
```

The third step is run another shell script to extract the files and add
the file extension ".nc".

```
 sh run_extrated_script.sh
```

And finally, you can use the NASA GISS to visualizing and analysing the dataset.


#

<p align="center"><b>Sincerely:</b> <a href="https://github.com/neemiasbsilva">Neemias B. da Silva</a></p>

#