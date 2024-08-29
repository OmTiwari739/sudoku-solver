# Sudoku Solver

## Overview

This is a Sudoku solver application built using Python's `tkinter` library. The application allows users to input Sudoku puzzles and provides a solution if one exists. The interface is designed to be intuitive, with cells automatically resizing to fit the window, and user-friendly features like automatic digit input and cell highlighting.

## Features

- **Sudoku Board**: A 9x9 grid for inputting Sudoku puzzles.
- **Solve Button**: Click to solve the Sudoku puzzle. If a solution is found, the board is updated with the solution. If no solution exists, an informational message is displayed.
- **Clear Button**: Clears all entries on the board, allowing users to input a new puzzle.
- **Automatic Cell Resizing**: The size of the cells adjusts automatically when resizing the window.
- **Digit Input Handling**: Only digits 1-9 are accepted, with automatic focus shift to the next cell.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/OmTiwari739/sudoku-solver.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd sudoku-solver
   ```

3. **Install Dependencies**:

   Ensure you have Python installed. This project uses the built-in `tkinter` library, so no additional packages are required.

## Usage

1. **Run the Application**:

   ```bash
   python sudoku_solver.py
   ```

2. **Input Sudoku Puzzle**:

   Enter digits (1-9) into the cells of the Sudoku grid. Empty cells should be left blank.

3. **Solve the Puzzle**:

   Click the "Solve" button to find a solution to the inputted Sudoku puzzle. If a solution exists, it will be displayed in the grid.

4. **Clear the Board**:

   Click the "Clear" button to reset the board and enter a new puzzle.

## Code Structure

- `sudoku_solver.py`: The main script containing the application logic and user interface.
- `README.md`: This file.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python's `tkinter` library for building the GUI.
- Sudoku algorithms for solving puzzles.
