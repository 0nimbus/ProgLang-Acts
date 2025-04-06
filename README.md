# Arithmetic Expression Compiler

A lexical analyzer and syntax parser for arithmetic expressions, implemented using Flex and Bison.

## Features
- Token classification (numbers, operators, parentheses)
- Syntax validation with error recovery
- Support for implicit multiplication (e.g., `2(3)` → `2*(3)`)
- Interactive expression evaluation

## Project Structure

.
├── src/
│ ├── calc.l # Lexer rules (Flex)
│ ├── calc.y # Parser rules (Bison)
│ └── main.c # Main program
├── Makefile # Build configuration
└── README.md # This file


## Build & Run
```bash
# Install dependencies (Ubuntu)
sudo apt install flex bison gcc make

# Compile
make clean && make

# Run interactively
./build/calculator

# Test sample input
echo "2*(3+1)" | ./build/calculator

SAMPLE OUTPUT:

NUMBER: 2
OPERATOR: *
PAREN: (
NUMBER: 3
OPERATOR: +
NUMBER: 1
PAREN: )
Valid expression