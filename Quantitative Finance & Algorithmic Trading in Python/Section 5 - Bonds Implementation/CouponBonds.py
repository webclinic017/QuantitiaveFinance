# Coupon Bonds

import math

class CouponBond:

    def __init__(self, principal, rate, maturity, interest_rate):
        # Principal Amount
        self.principal = principal
        # Coupon Interest Rate (paid annually)
        # 4% == 0.04
        self.rate = rate / 100
        # Date to Maturity
        self.maturity = maturity
        # Market Related Interest Rate (for discounting)
        # 4% == 0.04
        self.interest_rate = interest_rate / 100

    def present_value(self, x, n):
        return x / (1 + self.interest_rate) ** n # discrete model
        # return x * math.exp(-self.interest_rate * n) # continuous model

    def calculate_price(self):
        price = 0
        # discount the coupon payments
        for t in range(1, self.maturity+1):
            price = price + self.present_value(self.principal * self.rate, t)
        # discount principal amount
        price = price + self.present_value(self.principal, self.maturity)

        return price


if __name__ == '__main__':

    bond = CouponBond(1000, 10, 3, 4)
    print("Price of the bond: $%.2f" % bond.calculate_price())
    # Price of the bond: $1166.51