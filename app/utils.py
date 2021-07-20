import json
from django.conf import settings
# checking quality of parameter 
# based on http://www.binhlan.com/Chat-luong-nuoc-nuoi-tom-ca.html?fbclid=IwAR3d-6WkSvgOMufUlNOEKBr3gOIPfnmUgkTtd5tq7LoN0DUUPhuNv-wkaGY#N7
def CheckQuality(key, value):
    MIN = settings.RULES['{}_min'.format(key)]
    MAX = settings.RULES['{}_max'.format(key)]
    print(MIN)
    print(MAX)
    return


def score(center_point, real_point, low, high):
    if real_point < low or real_point > high:
        return 0
    else:
        return abs(real_point - center_point)/((high-low)/2)


def poison_score(center_point, real_point, high):
    if real_point > high:
        return 0
    return (high - real_point)/(high-center_point)


def avg_score(temp, salinity, clarity, pH, alkalinity, oxygen, hydrogen_sulfide, amonia, nitrit):
    temp_score = score(25, temp, 20, 30)
    salinity_score = score(15, salinity, 5, 25)
    clarity_score = score(32.5, clarity, 30, 35)
    pH_score = score(8, pH, 7.5, 8.5)
    alkalinity_score = score(125, alkalinity, 100, 150)
    oxygen_score = 0
    if oxygen_score < 3.5:
        oxygen_score = 0
    elif oxygen_score > 5:
        oxygen_score = 1
    else:
        oxygen_score = (oxygen - 3.5)/ (5 - 3.5)
    hydrogen_sulfide_score = poison_score(0, hydrogen_sulfide, 0.03)
    amonia_score = poison_score(0, amonia, 0.1)
    nitrit_score = poison_score(0, nitrit, 0.2)    
    
    total_score = 100 * (temp_score + salinity_score + clarity_score + pH_score + alkalinity_score + oxygen_score + hydrogen_sulfide_score + amonia_score + nitrit_score)
    return total_score/9