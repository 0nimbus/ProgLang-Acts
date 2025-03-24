package main

import (
	"bufio"
	"database/sql"
	"fmt"
	"os"
	"strconv"
	"strings"

	_ "github.com/mattn/go-sqlite3"
)

var db *sql.DB

// Initialize database
func initDB() {
	var err error
	db, err = sql.Open("sqlite3", "tasks.db")
	if err != nil {
		fmt.Println("Error opening database:", err)
		os.Exit(1)
	}

	// Create tasks table if not exists
	query := `CREATE TABLE IF NOT EXISTS tasks (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		description TEXT,
		status TEXT
	);`
	_, err = db.Exec(query)
	if err != nil {
		fmt.Println("Error creating table:", err)
		os.Exit(1)
	}
}

// Add a task
func addTask() {
	fmt.Print("Enter task description: ")
	reader := bufio.NewReader(os.Stdin)
	task, _ := reader.ReadString('\n')
	task = task[:len(task)-1] // Trim newline

	_, err := db.Exec("INSERT INTO tasks (description, status) VALUES (?, 'Pending')", task)
	if err != nil {
		fmt.Println("Error adding task:", err)
	} else {
		fmt.Println("Task added successfully!")
	}
}

// List tasks
func listTasks() {
	rows, err := db.Query("SELECT id, description, status FROM tasks")
	if err != nil {
		fmt.Println("Error fetching tasks:", err)
		return
	}
	defer rows.Close()

	fmt.Println("\n--- Task List ---")
	for rows.Next() {
		var id int
		var description, status string
		rows.Scan(&id, &description, &status)
		fmt.Printf("%d. [%s] %s\n", id, status, description)
	}
	fmt.Println("-----------------")
}

// Mark task as done
func completeTask() {
	fmt.Print("Enter task ID to mark as completed: ")
	reader := bufio.NewReader(os.Stdin)
	taskID, _ := reader.ReadString('\n')
	taskID = taskID[:len(taskID)-1]

	_, err := db.Exec("UPDATE tasks SET status = 'Completed' WHERE id = ?", taskID)
	if err != nil {
		fmt.Println("Error updating task:", err)
	} else {
		fmt.Println("Task marked as completed!")
	}
}

// Delete task
func deleteTask() {
	fmt.Print("Enter task ID to delete: ")
	reader := bufio.NewReader(os.Stdin)
	taskID, _ := reader.ReadString('\n')
	taskID = taskID[:len(taskID)-1]

	_, err := db.Exec("DELETE FROM tasks WHERE id = ?", taskID)
	if err != nil {
		fmt.Println("Error deleting task:", err)
	} else {
		fmt.Println("Task deleted successfully!")
	}
}

// Main menu loop
func main() {
	initDB()
	defer db.Close()

	for {
		fmt.Println("\nTask Reminder Menu:")
		fmt.Println("1. Add Task")
		fmt.Println("2. List Tasks")
		fmt.Println("3. Complete Task")
		fmt.Println("4. Delete Task")
		fmt.Println("5. Exit")
		fmt.Print("Choose an option: ")

		reader := bufio.NewReader(os.Stdin)
		choiceStr, _ := reader.ReadString('\n')
		choiceStr = strings.TrimSpace(choiceStr) // Trim spaces & newlines
		choice, err := strconv.Atoi(choiceStr)

		if err != nil {
			fmt.Println("Invalid input, please enter a number.")
			continue
		}

		switch choice {
		case 1:
			addTask()
		case 2:
			listTasks()
		case 3:
			completeTask()
		case 4:
			deleteTask()
		case 5:
			fmt.Println("Goodbye!")
			return
		default:
			fmt.Println("Invalid choice, please try again.")
		}
	}
}
