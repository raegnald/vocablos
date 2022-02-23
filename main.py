import sqlite3

from wordle_types import Color, Letter, Word, Wordle


conn = sqlite3.connect('rae.db')

five_letter_words: Wordle = Wordle([Word(w[0]) for w in
  conn.execute('select word from spanish_words where length(word) == 5')])


def get_word():
  word = input('word: ')
  return word

def color_letter_to_color(letter):
  if letter == 'b':
    return Color.BLACK
  elif letter == 'g':
    return Color.GREEN
  elif letter == 'y':
    return Color.YELLOW

def get_colors():
  return [color_letter_to_color(letter) for letter in input('colors: ').split()]

def show_words():
  print('\n\n')
  for word in five_letter_words.words:
    print(' → ', word)
  print(len(five_letter_words), 'five-letter words\n')

while True:
  show_words()
  word = get_word()
  if word == 'q': exit(0)
  colors = get_colors()
  five_letter_words.filter(Word(word, colors))