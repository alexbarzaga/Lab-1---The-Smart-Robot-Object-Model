#Navigation System Class
class navigationSystem:
    def __init__(self, software) -> None:
        self._software = software

    def receiveMission(self):
        print("Operater submitted mission.")

    def runHealthCheck(self):
        print("Operater ran health scan.")

    def planRoute(self):
        print("Route planned.")  

    def publishRoute(self):
        print("Route published to robot.")

    def parkBot(self):
        print("Robot parked.")

    def routeStart(self):
        print("Route started.")

    def routeEnd(self):
        print("Route ended.")

    def findWorkerStation(self):
        print("Arrived at worker station.")

    def relevanceSort(self):
        print("Shelf relocated.") 

#Driving Sytem Class
class DrivingSystem:
    def __init__(self) -> None:
        print("Motor constructor")

    def go(self): 
        print(f"Robot began moving forward!")

    def stop(self): 
        print(f"Robot stopped!")

    def rotate(self,direction,degrees): 
        print(f"Robot rotated {direction} {degrees} degrees!")

#Power System Class
class PowerSystem:
    def __init__(self) -> None:
        print("Battery constructor")

    def __init__(self) -> None:
        print("Battery percentage constructor")

    def __init__(self) -> None:
        print("Timer constructor")

    def charging(self): 
        print(f"Battery charging!")

    def powerMotor(self): 
        print(f"Motor is alive!")

#Wheels Class
class Wheels:
    def __init__(self) -> None:
        print("Material constructor")

    def __init__(self) -> None:
        print("Size constructor")

    def __init__(self) -> None:
        print("Position constructor")

    def moveForward(self): 
        print(f"Wheels are spinning!")

#Collission Detection System Class
class CollissionDetectionSystem:
    def __init__(self) -> None:
        print("Sensor constructor")

    def __init__(self) -> None:
        print("Bumper constructor")

    def movementPermission(self, judgement): 
        print(f"Robot {judgement} move!")

    def reroute(self): 
        print(f"Reroute neccessary!")

    def obstacleDetected(self): 
        print(f"An obstacle has been detected!")

    def queuePositionOpen(self): 
        print(f"The queue has an open position!")

#Camera Class
class Camera:
    def __init__(self) -> None:
        print("Camera constructor")

    def readFloorBarcode(self, floorCode): #floor code is an integer ID
        print("Floor code scanned.")

    def readPodBarcode(self, podCode): #pod code is an integer ID
        print("Pod code scanned.")

Camera.readFloorBarcode("Robot", 11659)

#Lifting Mechanism Class
class LiftingMechanism:
    def __init__(self) -> None:
        print("Screw constructor")

    def lift(self, unitLift): 
        print(f"Screw is lifting {unitLift} units!")

    def lower(self, unitLower): 
        print(f"Screw is lowering {unitLower} units!")
