from car import Car

class UberVan(Car):
    typeCarAccepted=[]
    seatmaterial=[]
    __passenger=int

    def __init__(self, license, driver,typeCarAceepted,seatmaterial):
        super().__init__(license, driver)
        self.typeCarAceepted=typeCarAceepted
        self.seatmaterial=seatmaterial