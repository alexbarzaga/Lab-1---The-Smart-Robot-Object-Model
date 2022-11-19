class LiftingMechanism:
    def __init__(self) -> None:
        print("Screw constructor")

    def lift(self, unitLift): 
        print(f"Screw is lifting {unitLift} units!")

    def lower(self, unitLower): 
        print(f"Screw is lowering {unitLower} units!")