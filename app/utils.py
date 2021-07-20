import json
# checking quality of parameter 
# based on http://www.binhlan.com/Chat-luong-nuoc-nuoi-tom-ca.html?fbclid=IwAR3d-6WkSvgOMufUlNOEKBr3gOIPfnmUgkTtd5tq7LoN0DUUPhuNv-wkaGY#N7
def CheckQuality(temp, salinity, clarity, pH, alkalinity, oxygen, hydrogen_sulfide, amonia, nitrit, Ca, Mg, K):
    # temperature with  unit of Celcious degree
    if temp < 20 or temp > 30:
        if temp < 20:
            return "The temperature is too low, it should be higher than 20 Celcious degree"
        elif temp > 30:
            return "The temperature is too high, it should be lower than 30 Celcious degree"
    # salinity with unit of 1/1000
    if salinity < 5 or salinity > 25:
        if salinity < 5:
            return "The salinity of water is too low, it should be higher than 0.5%"
        elif salinity > 25:
            return "The salinity of water is too high, it should be lower than 2.5%"
    # clarity with unit of cm
    if clarity < 30 or clarity > 35:
        if clarity < 30:
            return "The clarity of water is too low, it should be higher than 30cm"
        elif clarity > 35:
            return "The clarity of water is too high, it should be lower than 35cm"
    if pH < 7.5 or pH > 8.5:
        if clarity < 7.5:
            return "The pH value is too low, it should be higher than 7.5"
        elif clarity > 8.5:
            return "The pH value is too high, it should be lower than 8.5"
    # aklanity with unit of mg/l
    if alkalinity < 100 or alkalinity > 150:
        if alkalinity < 100:
            return "The alkalinity is too low, it should be high than 100 mg/l"
        elif alkalinity > 150:
            return "The alkalinity is too high, it should be lower than 150 mg/l"
    # oxygen with unit of mg/l
    if oxygen < 5:
        return "The oxygen value is low, it should be higher than 5 mg/l"
    # hydrogen sulfide poison with unit of mg/l
    if hydrogen_sulfide > 0.03:
        return "The hydrogen sulfide (H2S) value is high, it should be lower than 0.03 mg/l"
    # amonia poison with unit of mg/l 
    if amonia > 0.1: 
        return "The amonia value is high, it should be lower than 0.1 mg/l"
    # nitrit poison with unit of mg/l
    if nitrit > 0.2:
        return "The nitrit value is high, it should be lower than 0.2 mg/l"
    # rate of minerals 
    if Mg/Ca != 3.2 or K/Ca != 0.9:
        return "The rate of Mg:Ca:K should be 3.2:1:0.9"


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