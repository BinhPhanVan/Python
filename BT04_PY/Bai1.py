import requests
import json
class DownloadCovidInfo:    
    def __init__(self):
        self.__data= requests.get('https://api.covid19api.com/summary').json()
    def get_all_data(self):
        print(self.__data)
    def get_data_by_country(self):
        data1= self.__data['Countries']
        for index in data1:
            print(f"{index['Country']} had {index['NewDeaths']} new deaths")
    def save_to_file(self, file):
        with open(f"{file}.json", "w") as f:
            json.dump(self.__data, f, indent=2)
DownloadCovidInfo1 = DownloadCovidInfo()
DownloadCovidInfo1.get_all_data()
DownloadCovidInfo1.get_data_by_country()
DownloadCovidInfo1.save_to_file('data')