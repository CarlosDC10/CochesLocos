import json
import requests
from  vehicle import Vehicle

class controllerV():

    def __init__(self):
        self.__vehicles = {} #key = plate; Value = Vehicle object

    def getvehicles(self):
        return len(self.__vehicles)

    def AddVehicle(self, plate, description, chasis, driverName):
        if(plate in self.__vehicles):
            return False
        else:
            self.__vehicles[plate] = Vehicle(plate, description,chasis,driverName)
            return True
    
    def DeleteVehicle(self,plate):
        if(len(self.__vehicles[plate].getOdometer())>0):
            return False
        else:
            del self.__vehicles[plate]
            return True

    def AddOdometer(self, plate, date, destination, origin):
        km = 0.0
        url = "https://distanceto.p.rapidapi.com/get"

        querystring = {"route":"[{\"t\":\""+origin+"\",\"c\":\"ES\"},{\"t\":\""+destination+"\",\"c\":\"ES\"}]","car":"true"}

        headers = {
            'x-rapidapi-host': "distanceto.p.rapidapi.com",
            'x-rapidapi-key': "498beeb34fmsh7558841455add94p17d283jsn987de2c3f201"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            km = (float(data["steps"][0]["distance"]["car"]["distance"]))/1000
        
        if(plate in self.__vehicles):
            veh = self.__vehicles[plate]
            veh.addOdometer(date, origin,destination,km)
            return True
        else:
            return False

    def ConfirmOdometer(self, plate, date):
        if(plate in self.__vehicles):
            if(date in self.__vehicles[plate].getOdometer()):
                self.__vehicles[plate].setTotalkm(self.__vehicles[plate].getOdometer()[date][2])
                line= str(self.__vehicles[plate].getHistory())+"\n\t-"+str(date)+"--"+str(self.__vehicles[plate].getOdometer()[date][0])+"--"+str(self.__vehicles[plate].getOdometer()[date][1])+"--"+str(self.__vehicles[plate].getOdometer()[date][2])
                self.__vehicles[plate].setHistory(line)
                del self.__vehicles[plate].getOdometer()[date]
                return True
            else:
                return False
        else:
            return False

    def ListVehicle(self, search):
        if(search in self.__vehicles):
            veh = self.__vehicles[search]
            return veh
        for ve in self.__vehicles:
            if(self.__vehicles[ve].getDriverName()==search):
                veh = self.__vehicles[ve]
                return veh
        return "The car could not be found"
        