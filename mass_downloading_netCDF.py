import requests
import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Main File Script")
parser.add_argument("-url_name", action="store", required=True,
                    help="Url using to request the problem", dest="url_name")
parser.add_argument("-begin_year", action="store", required=True,
                    help="The parameter was included for the begin dataset", dest="begin_year")
parser.add_argument("-end_year", action="store", required=True,
                    help="The parameter was included for chose the end year", dest="end_year")
parser.add_argument("-user_name", action="store", required=True,
                    help="You id user for get the dataset", dest="user_name")
parser.add_argument("-password", action="store", required=True,
                    help="You password for get the dataset", dest="password")

arguments = parser.parse_args()
url_name = arguments.url_name
begin_year = int(arguments.begin_year)
end_year = int(arguments.end_year)
user_name = arguments.user_name
password = arguments.password

years = np.arange(begin_year, end_year)

for year in years:
    url_name += "APHRO_MA_TAVE_025deg_V1808." + str(year) + ".nc.gz"
    r = requests.get(url=url_name, auth=(user_name, password), allow_redirects=True)
    open(str(year)+".gz", "wb").write(r.content)
