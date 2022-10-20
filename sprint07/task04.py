class Washing:
    def wash(self):
        print('Washing...')


class Rinsing:
    def rinse(self):
        print('Rinsing...')


class Spinning:
    def spine(self):
        print('Spinning...')


class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()
        self.startWashing()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spine()