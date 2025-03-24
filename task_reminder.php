<?php
// Simple Task Reminder App with Completion Status

$taskFile = "tasks.txt";

// Load tasks from file
function loadTasks() {
    global $taskFile;
    if (!file_exists($taskFile)) {
        return [];
    }
    return file($taskFile, FILE_IGNORE_NEW_LINES);
}

// Save tasks to file
function saveTasks($tasks) {
    global $taskFile;
    file_put_contents($taskFile, implode("\n", $tasks));
}

// Display menu
function showMenu() {
    echo "\nTask Reminder Menu:\n";
    echo "1. Add Task\n";
    echo "2. List Tasks\n";
    echo "3. Complete Task\n";
    echo "4. Delete Task\n";
    echo "5. Exit\n";
    echo "Choose an option: ";
}

// Load tasks
$tasks = loadTasks();

while (true) {
    showMenu();
    $choice = trim(fgets(STDIN));

    switch ($choice) {
        case "1":
            echo "Enter a new task: ";
            $task = trim(fgets(STDIN));
            if (!empty($task)) {
                $tasks[] = $task;
                saveTasks($tasks);
                echo "Task added!\n";
            }
            break;
        case "2":
            echo "\nYour Tasks:\n";
            foreach ($tasks as $index => $task) {
                echo ($index + 1) . ". " . $task . "\n";
            }
            break;
        case "3":
            echo "Enter task number to complete: ";
            $taskNum = trim(fgets(STDIN)) - 1;
            if (isset($tasks[$taskNum])) {
                if (strpos($tasks[$taskNum], "(Completed)") === false) {
                    $tasks[$taskNum] .= " (Completed)";
                    saveTasks($tasks);
                    echo "Task marked as completed!\n";
                } else {
                    echo "This task is already completed!\n";
                }
            } else {
                echo "Invalid task number!\n";
            }
            break;
        case "4":
            echo "Enter task number to delete: ";
            $taskNum = trim(fgets(STDIN)) - 1;
            if (isset($tasks[$taskNum])) {
                unset($tasks[$taskNum]);
                $tasks = array_values($tasks); // Reindex array
                saveTasks($tasks);
                echo "Task deleted!\n";
            } else {
                echo "Invalid task number!\n";
            }
            break;
        case "5":
            echo "Exiting Task Reminder. Goodbye!\n";
            exit;
        default:
            echo "Invalid option, please try again!\n";
    }
}
?>
