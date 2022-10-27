from controllerV import controllerV

controller = controllerV()

def addVehicle():
    plate = ""
    while(True):
        plate = input("Plate of the vehicle: ")
        if(len(plate)==7):
            plateNum = plate[:4]
            plateLet = plate[4:]
            if(plateNum.isdigit()):
                if(plateLet.isalpha()):
                    break
                else:
                    print("Plate Letters are incorrect")
            else:
                print("Plate numbers are incorrect")
        else:
            print("Plate length is incorrect")

    desc = input("Description of the vehicle: ")
    
    chasis = ""

    while(True):
        chasis = input("Chasis of the vehicle: ")
        if(len(chasis)==17):
            break
        else:
            print("Chasis length is incorrect")

    driverName = input("Driver name: ")

    if(controller.AddVehicle(plate, desc,chasis,driverName)):
        print("Vehicle added")
    else:
        print("The car has already been added previusly")

def deleteVehicle():
    plate = input("Plate of the car you want to delete: ")
    if(controller.DeleteVehicle(plate)):
        print("The car has been deleted")
    else:
        print("The car could not be deleted")

def addOdometer():
    plate = input("Enter the plate: ")
    date = input("Enter the date: ")
    origin = input("The city of origin: ")
    destination = input("The city of detination: ")
    km = controller.AddOdometer(plate,date, destination,origin)
    if(km>0):
        print(km)
        print("Odometer added")
    else:
        print("The car does not exists")

def confirmOdometer():
    plate = input("Enter the plate: ")
    date = input("Enter the date: ")
    if(controller.ConfirmOdometer(plate, date)):
        print("Odometer confirmed")
    else:
        print("The car nor the date does not exists")

def listVehicle():
    search = input("Plate or DriverName: ")
    veh = controller.ListVehicle(search)
    print("Plate:",veh.getPlate(),"\n\tDescription:",veh.getDescription(),"\n\tChasis:",veh.getChasis(),"\n\tDriver Name:",veh.getDriverName(),"\n\tOdometer:",veh.getOdometer(),"\n\tTotal Kms:",veh.getTotalKm(),"\n\tHistory:",veh.getHistory())

choice = 0
while(choice != 6):
    print("There are ",controller.getvehicles(),"cars")
    print("1-Add vehicle")
    print("2-Delete Vehicle")
    print("3-Add odometer")
    print("4-Confirm odometer")
    print("5-List vehicle")

    choice = int(input("Select an option: "))

    if(choice == 1):
        addVehicle()

    if(choice == 2):
        deleteVehicle()

    if(choice ==3):
        addOdometer()

    if(choice == 4):
        confirmOdometer()

    if(choice == 5):
        listVehicle()

    
