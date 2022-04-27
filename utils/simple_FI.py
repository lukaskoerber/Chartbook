import pandas as pd
import numpy as np
import math

from sympy import re

class Bond():
    """This class describes a bond. Primary reason for definition: Convenient data binding.
    """
    def __init__(self, nominal, coupon, full_years_left, ytm, price=None, periodicity=1, time_until_next_payment=0):
        self.nominal = nominal
        self.price = price
        self.full_years_left = full_years_left
        self.coupon = coupon
        self.ytm = ytm
        self.periodicity = periodicity
        self.time_until_next_payment = time_until_next_payment

    def get_price(self):
        if self.price == None:
            return bond_price(self)
        else:
            return self.price
    
    def get_maturity(self):
        return self.time_until_next_payment + self.full_years_left

    def get_cashflow_profile(self):
        cashflow_profile = {i + self.time_until_next_payment: self.coupon / self.periodicity for i in np.arange(0, self.full_years_left, 1 / self.periodicity)}
        cashflow_profile[self.get_maturity()] += self.nominal
        return cashflow_profile


def pv_t(cf,y,t):
    return (cf) * math.exp(-y*t)

def bond_price(bond: Bond):
    sum=0
    for t in range(1, bond.get_maturity() + 1):
        sum+= pv_t(bond.coupon, bond.ytm, t)

    sum+=pv_t(bond.nominal, bond.ytm, bond.get_maturity())
    return sum

def ytm_on_bond():
    """This function takes the 
    """
    pass

