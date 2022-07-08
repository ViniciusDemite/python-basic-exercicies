import random
import string
import re

class Password():
  def __init__(self, length: int):
    self._length = length
    self._special_chars = re.sub(r'([^#$@!&\*\-\_])', '', string.punctuation)

  @property
  def length(self) -> int:
    return self._length

  def create_password(self) -> str:
    chars_qtd = self._chars_qtd()
    print(chars_qtd)
    uppercase_chars = random.choices(string.ascii_uppercase, k=chars_qtd)
    lowercase_chars = random.choices(string.ascii_lowercase, k=chars_qtd)
    digits = random.choices(string.digits, k=chars_qtd)
    special_chars = random.choices(
        self._special_chars, k=chars_qtd
      )

    password = uppercase_chars + lowercase_chars + digits + special_chars
    password = random.choices(password, k=self.length)

    return ''.join(password)

  def _chars_qtd(self) -> str:
    new_length = self.length ** random.randint(1, 5)
    new_length -= (self.length + random.uniform(100, 10000))

    return round(
        new_length / self.length * random.randint(2, 10)
    )