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
        self.pH               = round(uniform(6, 10),2)
        self.temp             = round(uniform(10,30),2)
        self.salinity         = round(uniform(10,25),2)
        self.alkalinity       = round(uniform(70,150),1)
        self.oxygen           = round(uniform(5,7),1)
        self.hydrogen_sulfide = round(uniform(0.01, 0.014),4)
        self.amonia           = round(uniform(0.05, 0.1),3)
        self.nitrit           = round(uniform(0.1, 0.2),2)
