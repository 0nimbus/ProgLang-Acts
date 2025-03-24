#!/usr/bin/perl
use strict;
use warnings;
use DBI;
use Term::ReadKey;

# Database setup
my $db = "tasks.db";
my $dbh = DBI->connect("dbi:SQLite:dbname=$db","","",{ RaiseError => 1, AutoCommit => 1 });

# Create table if not exists
$dbh->do("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, status TEXT)");

# Function to add a task
sub add_task {
    print "Enter new task: ";
    my $task = <STDIN>;
    chomp $task;
    $dbh->do("INSERT INTO tasks (task, status) VALUES (?, 'Pending')", undef, $task);
    print "Task added!\n";
}

# Function to list tasks
sub list_tasks {
    my $sth = $dbh->prepare("SELECT id, task, status FROM tasks");
    $sth->execute();
    print "\n--- Task List ---\n";
    while (my @row = $sth->fetchrow_array) {
        print "$row[0]. [$row[2]] $row[1]\n";
    }
    print "-----------------\n";
}

# Function to mark a task as done
sub complete_task {
    print "Enter task ID to mark as completed: ";
    my $task_id = <STDIN>;
    chomp $task_id;
    $dbh->do("UPDATE tasks SET status = 'Completed' WHERE id = ?", undef, $task_id);
    print "Task marked as completed!\n";
}

# Function to delete a task
sub delete_task {
    print "Enter task ID to delete: ";
    my $task_id = <STDIN>;
    chomp $task_id;
    $dbh->do("DELETE FROM tasks WHERE id = ?", undef, $task_id);
    print "Task deleted!\n";
}

# Main menu loop
while (1) {
    print "\nTask Reminder Menu:\n";
    print "1. Add Task\n";
    print "2. List Tasks\n";
    print "3. Complete Task\n";
    print "4. Delete Task\n";
    print "5. Exit\n";
    print "Choose an option: ";

    my $choice = <STDIN>;
    chomp $choice;

    if ($choice == 1) {
        add_task();
    } elsif ($choice == 2) {
        list_tasks();
    } elsif ($choice == 3) {
        complete_task();
    } elsif ($choice == 4) {
        delete_task();
    } elsif ($choice == 5) {
        print "Goodbye!\n";
        last;
    } else {
        print "Invalid choice! Try again.\n";
    }
}
