class navigationSystem:
    def __init__(self, software) -> None:
        self._software = software

    def receiveMission(self):
        print("Operater submitted mission.")

    def runHealthCheck(self):
        print("Operater ran health scan.")

    def planRoute(self):
        print("Route planned.")       



class Encoder(navigationSystem):
    def __init__(self, encoder, software):
        super().__innit__(encoder, software)
        self._feedback = "No errors!"

    def sendFeedback(self, report):
        print(f"{report}") #message that the encoder returns to the operator


navigationSystem.runHealthCheck("Kiva")

Encoder.sendFeedback("Kiva", "Error found!")

