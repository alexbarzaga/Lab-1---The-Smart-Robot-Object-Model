class Gyroscope:
    def __init__(self) -> None:
        print("Gyroscope constructor")

    def adjustBalance(self, tilt, direction): #tilt is represented in degrees
        print(f"Pod weight shifted {tilt} degrees to the {direction}!")

Gyroscope.adjustBalance("Gyro",12,"right")