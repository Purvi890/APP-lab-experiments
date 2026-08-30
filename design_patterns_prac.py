class TravelStrategy:

    def travel(self):
        pass


class Car(TravelStrategy):

    def travel(self):
        print("Travelling by car")


class Bike(TravelStrategy):

    def travel(self):
        print("Travelling by bike")


class Bus(TravelStrategy):

    def travel(self):
        print("Travelling by bus")


class Traveller:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def travel(self):
        self.strategy.travel()


def main():

    traveller = Traveller(Car())

    traveller.travel()

    traveller.set_strategy(Bike())
    traveller.travel()

    traveller.set_strategy(Bus())
    traveller.travel()


if __name__ == "__main__":
    main()