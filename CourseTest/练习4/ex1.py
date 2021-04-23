"""Read in the file specified on the command line. Do a simple split() on whitespace to obtain all the words in the file. Rather than read the file line by line, it's easier to read it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file to a list of all the words that immediately follow that word in the file. The list of words can be be in any order and should include duplicates. So for example the key "and" might have the list ["then", "best", "then", "after", ...] listing all the words which came after "and" in the text. We'll say that the empty string is what comes before the first word in the file.

With the mimic dict, it's fairly easy to emit random text that mimics the original. Print a word, then look up what words might come next and pick one at random as the next work. Use the empty string as the first word to prime things. If we ever get stuck with a word that is not in the dict, go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a random.choice(list) method which picks a random element from a non-empty list.
"""

import random
import sys

def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  mimic_dict = {}
  with open(filename,'r') as f:
    lines = f.readlines()
    list = []
    for i in range(0,len(lines)):
      for word in lines[i].split():
         list.append(word)
    f.close()

  mimic_dict[''] = list[0]
  for i in range(0,len(list)-1):
    mimic_dict[list[i]] = list[i+1:]
  return mimic_dict


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  word = mimic_dict[word]
  for i in range(1,200):
    if word in mimic_dict:
      print(word, end=' ')
      if isinstance(mimic_dict[word],list):
        word = random.choice(mimic_dict[word])
      else: word = mimic_dict[word]
    else:
      word = ''
      word = mimic_dict[word]
      print(random.choice(mimic_dict[word]),end=' ')

  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('command line usage: python ex1.py text.txt')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')

if __name__ == '__main__':
  main()
