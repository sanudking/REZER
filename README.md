# REZER

A lightweight, efficient Lexical Analyzer (Lexer) and tokenizer engine built completely from scratch in Python. **REZER** is designed to read raw source code string inputs and break them down into structured, meaningful cryptographic or syntax tokens based on a deterministic lexical grammar.

## 🚀 Features

- **Custom Tokenization**: Instantly scans code strings and outputs formatted tokens with distinct types and literal values.
- **Modular Components**: Features a clean separation of concerns between token definitions, state scanning, and execution.
- **Pure Python**: Zero third-party dependencies required. Highly portable and lightweight.
- **Compiler Foundation**: Serves as a robust structural foundation for custom Abstract Syntax Tree (AST) parsers or interpreters.

## 📂 Project Structure

The codebase is organized into three foundational modules:

*   `tokens.py` — Defines the token types, constants, and structured classes.
*   `lexer.py` — Houses the primary state machine logic that processes character streams into discrete tokens.
*   `main.py` — The system entry point used to feed sample inputs, execute the lexer, and display token streams.

## ⚙️ Installation & Usage

### Prerequisites
Make sure you have Python 3.x installed on your computer.

### Quick Start
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com
   cd REZER
   ```

2. Run the main driver script to watch the tokenizer parse sample code:
   ```bash
   python main.py
   ```

## 🛠️ Architecture Overview

The pipeline executes through a traditional compiler front-end workflow:

