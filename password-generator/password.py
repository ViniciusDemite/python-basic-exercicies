import random
import string
import re

class Password():
  def __init__(self, length: int):
    self._length = length
    self._special_chars = re.sub(r'([#$@!&\*\-\_])', string.string.punctuation)

  @property
  def length(self) -> int:
    return self._length

  @property
  def chars_qtd(self) -> str:
    new_length = self.length ** random.randint(1, 5)
    new_length -= (self.length + random.uniform(100, 10000))

    return round(
      new_length / self.length * random.randint(2, 10)
    )

  def create_password(self) -> str:
    uppercase_chars = random.choices(string.ascii_uppercase, k=self.chars_qtd)
    lowercase_chars = random.choices(string.ascii_lowercase, k=self.chars_qtd)
    digits = random.choices(string.digits, k=self.chars_qtd)
    special_chars = random.choices(
        self._special_chars, k=self.chars_qtd
      )

    password = uppercase_chars + lowercase_chars + digits + special_chars
    password = random.choices(random.shuffle(password), k=self.length)

    return ''.join(password)