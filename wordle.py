word = "START"

def makeAGuess(guess):
  hint = ""
  guess = guess.upper()
  for i in range(len(guess)):
    if word[i] == guess[i]:
      hint += 'G'
    elif guess[i] in word:
      hint += 'Y'
    else:
      hint += '-'
  return hint

print("Let's play wordle! \nGuess the Wordle in 6 tries. Each guess must be a valid 5-letter word. For each guess, a hint will tell you how many letters you've guessed correctly. A G represents a letter in the word and in the correct spot.. A Y represents a letter in the word but in the wrong spot. A - represents a letter not in the word in any spot.\n")

for i in range(6):
  guess = input(f"Guess #{i+1}: ")
  hint = makeAGuess(guess)
  print(hint)

  if hint == 'GGGGG':
    print("Congrats! You won!\n")
    break

if hint != 'GGGGG':
  print("Sorry, you lost...\n")