# Conway's Game of Life

A simulation of Conway's Game of Life built using Python and Pygame.

## About the Project

Conway's Game of Life is a cellular automaton created by mathematician John Horton Conway. It simulates the evolution of living and dead cells on a grid using a set of simple rules.

Although the rules are simple, they can produce complex and interesting patterns over time.

## Features

- Interactive grid where users can click cells to toggle their state.
- Real-time simulation of cell generations.
- Play and pause functionality.
- Adjustable simulation speed.
- Graphical visualization using Pygame.

## Rules of the Game

Each cell has eight neighboring cells. Its next state depends on the number of living neighbors.

1. Underpopulation: A living cell with fewer than two living neighbors dies.
2. Survival: A living cell with two or three living neighbors survives.
3. Overpopulation: A living cell with more than three living neighbors dies.
4. Reproduction: A dead cell with exactly three living neighbors becomes alive.

All cells update simultaneously in each generation.

## Controls

| Input | Action |
|---|---|
| Mouse click | Toggle a cell between alive and dead |
| Spacebar | Start or pause the simulation |
| Up Arrow | Increase simulation speed |
| Down Arrow | Decrease simulation speed |
| 0 | Set simulation speed to 1 FPS |
| 1 | Set simulation speed to 60 FPS |

## Technologies Used

- Python
- Pygame

## Installation

### Step 1: Install Python

Download and install Python from https://www.python.org/downloads/

### Step 2: Install Pygame

Open your terminal and run:

    pip install pygame

### Step 3: Clone the Repository

Run the following command,

    git clone https://github.com/N-RAMCHARAN-REDDY/conways-game-of-life.git

### Step 4: Run the Game

Open the project folder in your terminal and execute:

    python conway's game of life2.py


## Implementation Details

- The grid is represented using a two-dimensional Python list.
- Each cell is represented by 1 for alive and 0 for dead.
- A function counts the living neighbors of each cell.
- A new grid is created for each generation to ensure that all cells update simultaneously.
- Pygame handles graphics, keyboard input, mouse interaction, and simulation timing.

## Future Improvements

- Add a reset and clear-grid option.
- Add random initial cell patterns.
- Improve neighbor-counting logic and simulation performance.
- Add options to save and load patterns.

## Acknowledgements

Inspired by John Horton Conway's Game of Life.

## Author

N-RAMCHARAN-REDDY
