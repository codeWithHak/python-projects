# 🎮 Number Guessing Game

A command-line game where you guess a random number between 1-100 based on your chosen difficulty level. Features include a timer, error handling, and replay options.

## ✨ Features

- **Multiple Difficulty Levels**
  - Easy: 10 chances
  - Medium: 5 chances
  - Hard: 3 chances
  
- **User-Friendly Experience**
  - Smart error handling for invalid inputs
  - Time tracking for each game session
  - Higher/lower hints to guide your guesses
  - Replay option without restarting the program
 
## 🛣️ Project Guideleines
This number guessing game is based on the project guidelines from [roadmap.sh/projects/number-guessing-game](https://roadmap.sh/projects/number-guessing-game).
 
## ⚡ How to Run

Requires Python 3:
```bash
python main.py
```

## 🖥️ Game Preview

```
----- Welcome to the Number Guessing Game -----
=======================================================
I'm thinking of a number between 1 and 100
You have multiple chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice (1,2,3): 2

Great you selected Medium difficulty.
Enter your guess: 50
Incorrect! Number is less than 50

Enter your guess: 20
Incorrect! Number is greater than 20

Enter your guess: 35
Correct! You won
You took 8.12 seconds to guess

Do you want to play again? (Y/N)
```
## 🧠 What I Learned

- Generating random values
- Tracking execution time
- Handling input validation
- Structuring game flow logic
- Creating replayable CLI applications

## 💡 Future Improvements

- Implement a hint system that provides clues to the user if they are stuck
- Keep track of the user's high score (i.e., the fewest number of attempts it took to guess the number under a specific difficulty level)

## 🔗 More Projects

This project is part of my Python learning journey. View all projects at [Python Projects](https://github.com/codeWithHak/python-projects).
