import enum
from sys import setswitchinterval
from unidecode import unidecode


class Color(enum.Enum):
  NONE = 0
  BLACK = 1
  YELLOW = 2
  GREEN = 3
  TEMP_GREEN = 4


class Letter:
  def __init__(self, character, color: Color = Color.NONE):
    if len(character) != 1 and not character.isalpha():
      raise ValueError(
        f'The character must be one and alphanumeric, instead got {character}')
    self.character = unidecode(character).lower() # normalizing words
    self.color = color

  def __str__(self):
    return self.character


class Word:
  def __init__(self, letters: str, colors: list[Color] = None):
    if len(letters) != 5:
      raise Exception(
        f'A word must be 5 letters long, not {len(letters)} as in {letters}')

    if colors is None:
      colors = [Color.NONE] * len(letters)
    
    self.letters = [Letter(l, c) for l, c in zip(letters, colors)]

  def contains(self, letter):
    return letter in self.letters

  def contains_in(self, index, letter: str):
    return self.letters[index].character == letter

  def contains_from(self, i, letter: str):
    for j in range(i, len(self.letters)):
      if self.contains_in(j, letter):
        return True

  def mark(self, index, color: Color):
    self.letters[index].color = color

  def __str__(self):
    return ''.join(str(letter) for letter in self.letters)


class Wordle:
  def __init__(self, words: list[Word]):
    self.words = words

  def filter(self, word: Word):
    for i, letter in enumerate(word.letters):
      if letter.color == Color.BLACK:
        self.words = [w for w in self.words
          if not w.contains_from(i, letter.character)]

    for i, letter in enumerate(word.letters):
      if letter.color == Color.GREEN:
        self.words = [w for w in self.words
          if w.contains_in(i, letter.character)]

    for i, letter in enumerate(word.letters):
      if letter.color == Color.YELLOW:
        self.words = [w for w in self.words
          if w.letters[i] != letter
            # and w.contains(letter.character)
        ]

    for w in self.words:
      for i in range(len(w.letters)):
        w.mark(i, Color.NONE)


  def __len__(self):
    return len(self.words)