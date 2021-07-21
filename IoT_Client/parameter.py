from random import uniform

class Parameters():
    def __init__(self, pH = 0, temp = 0, salinity = 0
            , alkalinity = 0, oxygen = 0, hydrogen_sulfide = 0
            , amonia = 0, nitrit = 0):
        self.pH               = pH 
        self.temp             = temp
        self.salinity         = salinity
        self.alkalinity       = alkalinity
        self.oxygen           = oxygen
        self.hydrogen_sulfide = hydrogen_sulfide
        self.amonia           = amonia
        self.nitrit           = nitrit
        pass

    def update_random(self):
        self.pH               = round(uniform(7.5, 7.7),2)
        self.temp             = round(uniform(21,22),2)
        self.salinity         = round(uniform(15,16),2)
        self.alkalinity       = round(uniform(100,110),1)
        self.oxygen           = round(uniform(5,7),1)
        self.hydrogen_sulfide = round(uniform(0.01, 0.014),4)
        self.amonia           = round(uniform(0.2, 0.25),3)
        self.nitrit           = round(uniform(0.8, 0.9),2)
