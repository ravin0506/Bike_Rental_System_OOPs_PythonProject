class Bikeshop:
    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Available Bikes:-", self.stock)

    def RentForBike(self, Qnt):

        if Qnt <= 0:
            print('Entered Value should be >=0')
            print("Available Bikes:-", self.stock)
        elif Qnt > self.stock:
            print('Entered value is greater than Available Bikes')
            print("Available Bikes:-", self.stock)
            print()
        else:
            print("Total Price:-ReqQnt" + "*" + "100rs" + "=", Qnt * 100)
            print("Available Bikes:-", self.stock)


while True:
    obj = Bikeshop(100)
    UserChoice = int(input("""
    1. Display Stocks
    2. Rent A BIke
    3. Exit
    """))

    if UserChoice == 1:
        obj.displayBike()
    elif UserChoice == 2:
        n = int(input("Enter The required Qty-:"))
        obj.RentForBike(n)
    else:
        break
