import re


class Person:
  def __init__(self, name: str, age: int, cpf: str):
    self._name = name
    self._age = age
    self._cpf = cpf

  @property
  def name(self):
    return self._name

  @property
  def age(self):
    return self._age

  @property
  def cpf(self):
    return self._cpf

  @cpf.setter
  def cpf(self, cpf: str):
    if len(cpf) != 11:
      raise ValueError(f'O CPF {cpf} tem mais de 11 caracteres!!!')

    self._cpf = cpf