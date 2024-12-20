# AI Snake Game

## Index
- [Overview](#overview)
- [Features](#features)
- [Game Details](#game-details)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is a 2D Snake game where the player is an AI that uses the A* search algorithm to navigate the game. The AI controls the snake to move towards the apple, which changes position in each level. The game is developed using Python and Pygame.

## Features

- **AI-controlled Snake**: The AI uses the A* search algorithm to find the shortest path to the apple.
- **Multiple Levels**: The game includes multiple levels, each with a different apple position.
- **Obstacles**: Optionally, obstacles can be added to the game, requiring the AI to avoid them while navigating towards the apple.

## Game Details

- **Algorithm**: The A* search algorithm is used to determine the snake's path. If obstacles are added, the algorithm will run twice in each step to check both the desired goal (apple) and the obstacles.
- **Levels**: The game contains up to 5 levels, with increasing difficulty.
- **Programming Language**: Python
- **Game Development**: Pygame

## How to Play

The player does not control the snake directly. Instead, the AI navigates the snake through the game, aiming to reach the apple in the shortest path possible. The position of the apple changes with each level, and obstacles can be added to increase the complexity.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/AbdelrahmanMNaser/AI_Snake.git
2. Navigate to the project directory:
   ```sh
   cd AI_Snake
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt

## Running the game
To start the game, run the following command:
```sh
python main.py
```

## Future Enhancements
- Add more levels with increasing difficulty.
- Introduce different types of obstacles.
- Improve the AI algorithm for better performance.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
