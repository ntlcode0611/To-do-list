A simple command-line todo list manager built in Python that allows users to add, view, and manage their daily tasks with persistent data storage.

## Features

- **Add Tasks**: Add new items to your todo list
- **View Tasks**: Display all current tasks with numbered indexing
- **Mark Complete**: Remove completed tasks from your list
- **Persistent Storage**: Tasks are automatically saved to and loaded from a text file
- **User-friendly Interface**: Clean menu-driven interface for easy navigation

## Requirements

- Python 3.x
- No additional dependencies required (uses only built-in Python libraries)

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. Navigate to the project directory

## Usage

1. Run the application:
   ```bash
   python todo_app.py
   ```

2. Use the menu options:
   - **1**: Add a new task to your list
   - **2**: Display all current tasks
   - **3**: Mark a task as complete (removes it from the list)
   - **0**: Exit the application

## File Structure

```
todo-list/
├── todo_app.py          # Main application file
├── data.txt             # Persistent storage file (created automatically)
└── README.md            # This file
```

## How It Works

The application uses a simple text file (`data.txt`) to store tasks persistently. When you start the program:

1. Tasks are loaded from `data.txt` into memory
2. You can perform operations (add, view, delete tasks)
3. Changes are automatically saved back to the file
4. Your tasks persist between program sessions

## Code Structure

- `Main_menu()`: Displays the main menu options
- `addItem()`: Handles adding new tasks and saving to file
- `view_Menu()`: Displays all current tasks with numbering
- `deleteItem()`: Removes completed tasks and updates the file
- `doneItem()`: Provides user feedback and pause functionality

## Example Usage

```
Menu
1. Add Item
2. Display Item
3. Mark Item
0. Exit
Please select your choice: 1
Add your task: Complete Python assignment
You have done it!
Press any button to continue:
```

## Future Enhancements

- Task priority levels
- Due date functionality
- Task categories/tags
- Search and filter capabilities
- GUI interface
