from abc import ABC, abstractstaticmethod
from typing import Union

class Account(ABC):
  def __init__(self, agency: str, number: str, balance: Union[int, float]):
    self._agency = agency
    self._number = number
    self._balance = balance

  @property
  def agency(self):
    return self._agency
    
  @property
  def number(self):
    return self._number

  @property
  def balance(self):
    return self._balance

  @balance.setter
  def balance(self, balance: Union[int, float]):
    self._balance = balance

  def deposit(self, value: Union[int, float]):
    self.balance += value

  @abstractstaticmethod
  def withdraw(self, withdraw_value: Union[int, float]):
    pass