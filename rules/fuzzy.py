import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Generate universe variables
#   * tempity and service on subjective ranges [0, 10]
#   * WQI has a range of [0, 25] in units of percentage points
def add(temp, salt, pH, DO):
    cnt_key_word = {
        'Very_Low' : 0,
        'Low' : 0, 
        'Normal' : 0, 
        'High' : 0, 
        'Very_High' : 0,
    }
    cnt_key_word[temp] += 1
    cnt_key_word[salt] += 1
    cnt_key_word[pH]   += 1
    cnt_key_word[DO]   += 1
    if (cnt_key_word['Normal'] == 4):
        return 'Excellent'
    elif (cnt_key_word['Normal'] == 3 and cnt_key_word['Low'] + cnt_key_word['High'] == 1):
        return 'Good'
    elif (cnt_key_word['Normal'] == 2 and (cnt_key_word['Low'] == 2 or cnt_key_word['High'] == 2)):
        return 'Regular'
    else:
        return 'Poor'
# Def(chi so, chi so, chi so)
temp = ctrl.Antecedent(np.arange(0, 50, 1), 'temp')
salt = ctrl.Antecedent(np.arange(0, 36, 1),'salt')
pH   = ctrl.Antecedent(np.arange(0, 14, .5),'pH')
DO   = ctrl.Antecedent(np.arange(0, 8, .5),'DO')

WQI = ctrl.Consequent(np.arange(0, 1, 0.1), 'WQI')

# Generate fuzzy membership functions
temp['Low'] = fuzz.trapmf(temp.universe, [0,0,19,21])
temp['Normal'] = fuzz.trapmf(temp.universe, [19, 21, 29,31])
temp['High'] = fuzz.trapmf(temp.universe, [29, 31, 50, 50])

salt['Low'] = fuzz.trapmf(salt.universe, [0,0,14,16])
salt['Normal'] = fuzz.trapmf(salt.universe, [14, 16, 22,24])
salt['High'] = fuzz.trapmf(salt.universe, [22,24,36,36])

pH['Very_Low']      = fuzz.trapmf(pH.universe,[0,0,3.5,4.5])
pH['Low']           = fuzz.trapmf(pH.universe,[3.5,4.5,6,7])
pH['Normal']        = fuzz.trapmf(pH.universe,[6,7,9,10])
pH['High']          = fuzz.trapmf(pH.universe,[9,10,10.5,11.5])
pH['Very_High']     = fuzz.trapmf(pH.universe,[10.5,11.5,14,14])

#Dissolved Oxygen value sets
DO['Very_Low']     = fuzz.trapmf(DO.universe,[0,0,1.5,2.5])
DO['Low']      = fuzz.trapmf(DO.universe,[1.5,2.5,4.5,5.5])
DO['Normal']   = fuzz.trapmf(DO.universe,[4.5,5.5,8,8])


WQI['Poor'] = fuzz.trapmf(WQI.universe, [0, 0, 0.1, 0.2])
WQI['Regular'] = fuzz.trapmf(WQI.universe, [0.1, 0.2, 0.4, 0.5])
WQI['Good'] = fuzz.trapmf(WQI.universe, [0.4, 0.5, 0.7, 0.8])
WQI['Excellent'] = fuzz.trapmf(WQI.universe, [0.7, 0.8, 1, 1])

#Set Rules
list_temp_salt =['Low', 'Normal', 'High']
list_pH = ['Very_Low', 'Low', 'Normal', 'High', 'Very_High']
list_DO   = ['Very_Low', 'Low', 'Normal']
n = 0
rule = []
for temps in list_temp_salt:
    for salts in list_temp_salt:
        for pHs in list_pH:
            for DOs in list_DO:
                rls = ctrl.Rule(temp[temps] & salt[salts] & pH[pHs] & DO[DOs], WQI[add(temps,salts, pHs, DOs)])
                rule.append(rls)

WQI_ctrl = ctrl.ControlSystem(rule)
WQIs = ctrl.ControlSystemSimulation(WQI_ctrl)

def Compute(t, s, p, d):
    WQIs.input['temp'] = t
    WQIs.input['salt'] = s
    WQIs.input['pH'] = p
    WQIs.input['DO'] = d
    WQIs.compute()
    return WQIs.output['WQI']
