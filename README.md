# The Russian Roulette Game

### Description:
This project is an interactive simulation of **Russian Roulette Game** where the player faces a revolver. This revolver has a 6-space drum, and the player chooses how many bullets to load. The player has the option to spin the drum or pull the trigger on each turn. Also, this game can be played by two players in real life just taking turns.

The goal of the game is simple: If the players pull the trigger and the bullet is fired, the game ends with a **"GAME OVER"** message. But if no bullet is fired, the player can continue playing and stay alive. Also, the player has the option of spinning the revolver's drum at any time, which alters the randomness of the shots.

## Features:
- **Choice of number of bullets**: The player has the option of choosing how many bullets will have the revolver drum between 1 to 5 and an Input Validator will make sure that the player has prompt the right number. If the players enter any other number, the program will ask again.
- **Randomness**: The bullets in the revolver are shuffled randomly when the player decides to spin the revolver's drum. The player can spin the drum whenever he wants.
- **Visual messages**: ANSI colors and ASCII are used in the terminal window to give an immersive visual experience:
  - The tittle of the game "Russian Routlette" appears in large size.
  - "You're alive" appears in green.
  - "GAME OVER" appears in red.
  - "Spinning..." appears in yellow.
- **Interactive options**: The player can choose between "s" to spin the drum or "p" to pull the trigger.

## How to Run the Game:
1. Clone or download this repository to your computer.
2. The sound 1 is Squid game OST and sound 2 revolver shot must be changed in the path where you have the sound files.
3. Ensure that you have Python 3.x installed.
