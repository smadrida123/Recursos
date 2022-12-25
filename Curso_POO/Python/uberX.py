from car import Car

class UberX(Car):
    brand=str
    model=str
    __passenger=4

    def __init__(self, license, driver,brand,model):
        super().__init__(license, driver)
        self.brand=brand
        self.model=model

    def set_passenger():
        return self.__passenger