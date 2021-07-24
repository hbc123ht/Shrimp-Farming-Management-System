from random import paretovariate
import json

from rest_framework import response
from parameter import Parameters
import requests
import time

def main():
    parameters = Parameters()
    while True:
        parameters.update_random()
        data = {
                "password"        : 'hbc123vnjp', #Dien password nguoi dung
                "pH"              : parameters.pH,
                "temp"            : parameters.temp,
                "salinity"        : parameters.salinity,
                "alkalinity"      : parameters.alkalinity,
                "oxygen"          : parameters.oxygen,
                "hydrogen_sulfide": parameters.hydrogen_sulfide,
                "amonia"          : parameters.amonia,
                "nitrit"          : parameters.nitrit,
                }
        print(data)
        try:
            response = requests.put("http://127.0.0.1:8000/update_params/test/", json = data)
        except:
            pass
        time.sleep(5)

if __name__ == "__main__":
    main()
