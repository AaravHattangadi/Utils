import random

def scramble(word):
  letters = list(word)
  random.shuffle(letters)
  scramble_word = ""
  for i in letters:
    scramble_word = scramble_word + i
  return scramble_word

while (True):
  word = input("What word do you want to scramble:\n\n")
  if (word.lower().strip() == "egg"):
    print("\negg scrambled is a scrambled egg\n")
  elif (word.lower().strip() == "eggs"):
    print("\neggs scrambled are scrambled eggs\n")
  else:
    print("\n" + word, "scrambled is", scramble(word), "\n")