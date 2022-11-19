class DrivingSystem:
    def __init__(self) -> None:
        print("Motor constructor")

    def go(self): 
        print(f"Robot began moving forward!")

    def stop(self): 
        print(f"Robot stopped!")

    def rotate(self,direction,degrees): 
        print(f"Robot rotated {direction} {degrees} degrees!")

