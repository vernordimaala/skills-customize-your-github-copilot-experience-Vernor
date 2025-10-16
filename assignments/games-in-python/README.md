

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. Practice string manipulation, loops, conditionals, and random selection while creating an interactive console game.

## 📝 Tasks

### 🛠️  Hangman Game Logic

#### Description
Create the main game loop for Hangman. The program should randomly select a word, accept letter guesses, and display the current progress. Track incorrect guesses and end the game with a win or lose message.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept letter guesses from the user
- Show current progress (e.g., _ _ _ format for unrevealed letters)
- Track and display the number of incorrect guesses remaining
- End when the word is guessed or attempts are exhausted
- Display appropriate win/lose messages

Example:
```
Word: _ _ _ _ _
Guess a letter: a
Word: _ a _ _ _
Incorrect guesses left: 5
...etc...
```

### 🛠️  Word List & Replay Feature

#### Description
Enhance your game by allowing replay and using a larger, more interesting word list. After each game, ask the player if they want to play again.

#### Requirements
Completed program should:

- Use a list of at least 10 words for random selection
- Ask the player if they want to play again after each game
- Restart the game if the player chooses to replay
- Exit gracefully if the player chooses not to replay
