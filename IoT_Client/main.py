from random import paretovariate

from rest_framework import response
from parameter import Parameters
import requests
import time

def main():
    parameters = Parameters()
    while True:
        parameters.update_random()
        data = {
                "password"  : 'hieu01022001', #Dien password nguoi dung
                "ph"        : parameters.ph,
                "temp"      : parameters.temp,
                "salinity"  : parameters.salinity,
                "alkalinity": parameters.alkalinity,
                "oxygen"    : parameters.hydrogen_sulfide,
                "amonia"    : parameters.amonia,
                "nitrit"    : parameters.nitrit,
                "Ca"        : parameters.Ca,
                "Mg"        : parameters.Mg,
                "K"         : parameters.K,
                }
        print(data)
        response = requests.put("http://127.0.0.1:8000/update_params/rikikudohust/", data)
        time.sleep(5)

if __name__ == "__main__":
    main()
