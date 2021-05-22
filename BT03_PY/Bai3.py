import requests
import json
class DownloadCovidInfo:    
    def __init__(self):
        self.__url = 'https://api.covid19api.com/dayone/country/south-africa/status/confirmed'
    def get_all_data(self):
        return requests.get(self.__url).__dict__
    def get_data_by_country(self):
        return requests.get(self.__url).__dict__
DownloadCovidInfo1 = DownloadCovidInfo()
data = (DownloadCovidInfo1.get_all_data())
# with open("students.json", "w") as f: # w= db
#     json.dump(data, f, indent=2)
# with open("students.json", "r") as f:
#  data =json.load(f)
data1 = list(data)
print(data1["Countries"])
