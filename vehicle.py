class Vehicle:
    def __init__(self, plate, description,chasis, driverName):
        self.__Plate = plate
        self.__Description = description
        self.__Chasis = chasis
        self.__DriverName = driverName
        self.__Odometer = {}
        self.__TotalKm = 0.0
        self.__History = ""

    def getPlate(self):
        return self.__Plate
        
    def getDescription(self):
        return self.__Description

    def getChasis(self):
        return self.__Chasis

    def getDriverName(self):
        return self.__DriverName

    def getOdometer(self):
        return self.__Odometer

    def getTotalKm(self):
        return self.__TotalKm

    def getHistory(self):
        return self.__History

    def setDescription(self, desc):
        self.__Description = desc

    def setDriverName(self, name):
        self.__DriverName = name

    def setOdometer(self, odo):
        self.__Odometer = odo

    def setTotalkm(self, tot):
        self.__TotalKm = tot

    def setHistory(self, hist):
        self.__History = hist

    def addOdometer(self, date, origin, destination, km):
        self.__Odometer[date] = (origin, destination, km)
