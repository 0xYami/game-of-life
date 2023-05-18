# Conway's Game of Life (Python)

This is an implementation of Conway's Game of Life in Python. The Game of Life is a cellular automaton devised by the mathematician John Horton Conway. It is a game with simple rules but can exhibit complex and fascinating behavior.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```shell
   git clone <repository-url>
   ```

2. Change into the project directory:

   ```shell
   cd game-of-life/Python
   ```

3. (Optional) Create a virtual environment:

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

## Usage

To run the Game of Life simulation, execute the following command:

```shell
python game-of-life.py
```

The simulation window will open, and you will see the Game of Life grid. The grid will update automatically with each generation based on the rules of the game. You can customize the grid size, initial density, and number of generations by modifying the parameters in the `game_of_life` function in the `game_of_life.py` file.

## Examples

To run the simulation with custom parameters, modify the following line in the `game_of_life.py` file:

```python
game_of_life(width=50, height=50, density=0.2, generations=100)
```

- `width`: Width of the grid (default: 50)
- `height`: Height of the grid (default: 50)
- `density`: Initial density of live cells (default: 0.2)
- `generations`: Number of generations to simulate (default: 100)

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
