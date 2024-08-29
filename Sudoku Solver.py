import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]))
                entries[i][j].config(fg='blue', font=('Arial', 18, 'bold'))
            else:
                entries[i][j].delete(0, tk.END)
            reset_cell_color(i, j)

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            try:
                num = int(entries[i][j].get())
            except ValueError:
                num = 0
            row.append(num)
        board.append(row)
    return board

def solve_sudoku():
    board = get_board()
    if solve(board):
        print_board(board)
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists for the given Sudoku board.")

def clear_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            reset_cell_color(i, j)

def reset_cell_color(row, col):
    if (row // 3 + col // 3) % 2 == 0:
        entries[row][col].config(bg=highlight_color, relief='solid', bd=1)
    else:
        entries[row][col].config(bg=entry_color, relief='solid', bd=1)

def move_focus(event):
    row, col = event.widget.grid_info()['row'], event.widget.grid_info()['column']
    next_col = (col + 1) % 9
    next_row = row + (col + 1) // 9
    if next_row < 9:
        entries[next_row][next_col].focus()

def on_input(event):
    if event.char.isdigit() and event.char != '0':
        event.widget.delete(0, tk.END)
        event.widget.insert(0, event.char)
        move_focus(event)
    else:
        event.widget.delete(0, tk.END)

def resize_window(event):
    cell_size = min(event.width, event.height) // 9
    for i in range(9):
        for j in range(9):
            entries[i][j].config(width=cell_size, font=('Arial', max(14, cell_size // 2), 'bold'))

root = tk.Tk()
root.title("Sudoku Solver")
root.configure(bg="#F0F0F0")
root.geometry('600x600')

bg_color = "#F0F0F0"
entry_color = "#FFFFFF"
highlight_color = "#DCE4F0"

entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, width=3, font=('Arial', 18, 'bold'), justify='center', bg=entry_color, relief='solid', bd=1)
        entry.grid(row=i, column=j, sticky='nsew', padx=1, pady=1)

        if (i // 3 + j // 3) % 2 == 0:
            entry.config(bg=highlight_color)

        entry.bind("<KeyRelease>", on_input)
        row_entries.append(entry)
    entries.append(row_entries)

solve_button = tk.Button(root, text="Solve", command=solve_sudoku, font=('Arial', 14, 'bold'), bg='#4CAF50', fg='white', relief='raised')
solve_button.grid(row=10, column=2, columnspan=2, pady=10, sticky='ew')

clear_button = tk.Button(root, text="Clear", command=clear_board, font=('Arial', 14, 'bold'), bg='#F44336', fg='white', relief='raised')
clear_button.grid(row=10, column=5, columnspan=2, pady=10, sticky='ew')

for i in range(9):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.bind('<Configure>', resize_window)

root.mainloop()
