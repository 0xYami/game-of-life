import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def game_of_life(width, height, density, generations):
    # Initialize the game grid
    state = np.random.choice([0, 1], size=(height, width), p=[1 - density, density])

    fig, ax = plt.subplots()
    img = ax.imshow(state, cmap='binary', interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, frames=generations, fargs=(img, state), interval=200, repeat=False)

    plt.show()

def update(frame_number, img, state):
    # Calculate the number of live neighbors for each cell
    neighbor_count = np.zeros_like(state)
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            neighbor_count[i, j] = count_neighbors(state, i, j)

    # Apply the rules of Conway's Game of Life
    next_state = np.where((state == 1) & ((neighbor_count < 2) | (neighbor_count > 3)), 0, state)
    next_state = np.where((state == 0) & (neighbor_count == 3), 1, next_state)

    img.set_data(next_state)
    state[:] = next_state[:]
    return img

def count_neighbors(state, row, col):
    height, width = state.shape
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_row = (row + i) % height
            neighbor_col = (col + j) % width
            count += state[neighbor_row, neighbor_col]
    return count

# Example usage
game_of_life(width=50, height=50, density=0.2, generations=100)
