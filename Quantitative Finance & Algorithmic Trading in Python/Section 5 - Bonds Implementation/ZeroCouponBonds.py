# Zero Coupon Bonds

class ZeroCouponBonds:

    def __init__(self, principal, maturity, interest_rate):
        # Principal Amount
        self.principal = principal
        # Date to Maturity
        self.maturity = maturity
        # Market Related Interest Rate (for discounting)
        # 4% == 0.04
        self.interest_rate = interest_rate / 100

    def present_value(self, x, n):
        return x / (1 + self.interest_rate)**n

    def calculate_price(self):
        return self.present_value(self.principal, self.maturity)

if __name__ == '__main__':

    bond = ZeroCouponBonds(1000, 2, 4)
    print("Price of the bond: $%.2f" % bond.calculate_price())
    # Price of the bond: $924.56