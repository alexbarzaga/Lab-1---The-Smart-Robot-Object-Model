class Accelerometer:
    def __init__(self) -> None:
        print("Accelerometer constructor")

    def increaseSpeed(self, base, increase):
        total = base + increase #total was created to show the new robot speed after being increased by x units
        print(f"Speed increased from {base} to {total}!")

    def decreaseSpeed(self, base, decrease):
        total2 = base - decrease #total2 was created to show the new robot speed after being increased by x units
        print(f"Speed decreased from {base} to {total2}!")

Accelerometer.decreaseSpeed("speed", 5, 2)