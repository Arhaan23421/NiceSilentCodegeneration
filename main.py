import random
#Rules:
#Choosing a letter from alphabet to fill out a word that we don't know
#Show a certain amount of blanks, depending on the length of the word
#Game ends when user runs out of lives or guesses correctly/incorrectly

#Data- alphabet, lives, word, oldLetters, [randomWords], gameMode (single or multiplayer)
word = ""
gameMode = 1
randomWords = ['Jazz', "Hello", "sports", "mountain", "basketball", "apostrophe"]
prevcorrectguess = []
prevwrongguess = []
#Functionality/Interactions- submitLetter(), guessWords(), checkLetter(), 
#                          updateLives(), Handles blanks -> printGameBoard(), getGuessWord()

#in multiplayer, one of the players chooses a word for another user to guess; in single player, the computer chooses a random word from the dictionary.
def getGuessWord():
  global word
  if gameMode == 2: 
    response = input("What word do you want to use?")
    response = response.strip()
    word = response
  #Get random word
  else :
    randInt = (random.randint(0, len(randomWords)-1))
    randomWord = randomWords[randInt]
    word = randomWord
# sees if 'guess' is the same as 'word'
def checkGuess(guess):
  if guess.lower() == word.lower():
    print ("nice job, you won")
    return True
  else:
    return False
  pass
def checkLetter(guess):
  if str(guess).lower() in word.lower():
    prevcorrectguess.append(guess)
  else: 
    prevwrongguess.append(guess)
  pass
  
# it displays the amount of blanks based off of the amount of charectars that are in the word the user is trying to guess, then display the correct letter the user guessed to the correct part
def printGameBoard():
  for letter in word:
    if letter in prevcorrectguess:
        print(letter, end= " ")
    else:
      print ("_", end=" " )

  submit()
  
#user types in what letters they are guesing to be in the word. But prevent users from typing in numbers
def submit():
  userguess = input("guess a letter")

  for num in range(0,10):
    if str(num) in userguess:
      print ("not allowed, put another word in")
      submit()
      return

  # if the length of userguess reater than 1 then they are guessing a word but if the charectars are less than or equal to one then they are guessing letters

  if len(userguess) > 1:
    if checkGuess(userguess):
      return
  else:
    checkLetter(userguess)
  printGameBoard()


#Main game start
getGuessWord()
printGameBoard()