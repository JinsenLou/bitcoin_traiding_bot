import numpy as np
import pandas as pd

class Asset:
    def __init__(self) -> None:
        self.money = 100
        self.tax = 0.02
        self.coin = 0

    def buy(self, coin_vlaue):
        money_in_market = self.money * (1 - self.tax)
        self.money = 0
        self.coin = money_in_market / coin_vlaue

    def sell(self, coin_value):
        self.money = self.coin * coin_value * (1 -self.tax)
        self.coin = 0