# python-foundations

My programming work while pursuing an Online BCA at Manipal University Jaipur, built alongside a self-directed 3-year roadmap toward becoming an AI/ML engineer. Started August 2026.

**Tech Stack & Tools:** Python 3, Git, Virtual Environments (`venv`), APIs (`requests`), Data Science (Pandas, NumPy, Matplotlib)

The repo is split into three main folders:
- **`Data_Science/`** — Data pipelines, `.csv` cleaning, aggregation (`.groupby()`), and visualization.
- **`projects/`** — real builds: fundamentals, file handling, APIs, and OOP.
- **`leetcode/`** — DSA practice problems and a running Problem Journal documenting the specific "what clicked" moments for every solution.

Each project follows the same reflection format: **what it does, why I built it, what I'd do differently.**

---

## ⚙️ How to Run

To run any of the command-line applications locally:

1. Clone this repository:
   `git clone https://github.com/rahuldegra1/python-foundations.git`
2. Navigate into the folder:
   `cd python-foundations`
3. (Optional but recommended) Set up a virtual environment:
   `python -m venv env`
   `source env/bin/activate`  *(On Windows use `.\env\Scripts\activate`)*
4. Run a specific script:
   `python projects/api_test.py`

---

## 📊 Data Science (`Data_Science/`)

### Regional Sales Pipeline (`002_pandas_load.py`)
**What it does:** Ingests a raw `.csv` dataset, cleans text into `datetime64` time objects, runs a Split-Apply-Combine aggregation (`.groupby()`) to summarize regional revenue, and visualizes the math using a Matplotlib bar chart.
**Why I built it:** To establish a fully functioning local Python data science environment, bypass Windows execution policies for pre-compiled C++ engines, and practice structural data analysis.
**What I'd do differently:** Now that the local CSV pipeline works perfectly, the next step is combining this logic with the `requests` library to pull live data directly from the internet.

---

## 🚀 Projects

### User Lookup Tool (API)
**What it does:** A command-line tool that dynamically fetches and parses live JSON data from an external server using the `requests` library, injecting user input into the URL via f-strings.
**Why I built it:** To practice network requests, JSON parsing, and completely isolating third-party dependencies using a Python virtual environment (`venv`).
**What I'd do differently:** Next time, I would add a `try/except` block to handle network errors gracefully (like if the computer loses internet connection while running the script) or to catch invalid user inputs if they type a letter instead of a number.

### Tic-Tac-Toe
**What it does:** A command-line two-player game. Maps a 3x3 grid to a single flat list (index 0-8), prints the board after every move, and checks all 8 win combinations.
**Why I built it:** To practice mapping 2D coordinates onto a 1D data structure, and to work with nested win-condition logic.
**What I'd do differently:** I originally had the draw-check run *before* the win-check, which meant a winning final move on the last empty square got misreported as a draw. Fixed it by reordering the checks. Next time, I'd refactor the board into a `Board` class from the start instead of a plain list.

### Dynamic Quiz App
**What it does:** A command-line trivia game that reads questions, four options, and the correct answer from an external `questions.csv` file using `csv.DictReader`.
**Why I built it:** To practice reading structured external data instead of hardcoding everything into the script.
**What I'd do differently:** Shuffle the question order and the answer options on each run so the quiz isnt identical every time. Also add input validation.

### Contact Book
**What it does:** Stores contacts as dictionaries in a list, with add, view, and delete options. Persists data to a text file (`contact.txt`).
**Why I built it:** To practice file persistence and using a `for...else` loop for the delete-by-name search.
**What I'd do differently:** Switch from manually parsing comma-separated lines to using Python's `json` module for storage.

### Number Guessing Game
**What it does:** The computer picks a random number; the player has 7 attempts to guess it, with "too high / too low" hints.
**Why I built it:** To practice `while` loops, attempt counting, and handling invalid input without crashing.
**What I'd do differently:** Track and display the player's best (fewest-attempts) score across rounds, and let the player choose a difficulty level.

### Rock, Paper, Scissors
**What it does:** Plays rounds against the computer using Python's `random` module, tracking stats across the session.
**Why I built it:** To practice conditional logic across three possible choices and outcomes.
**What I'd do differently:** Replace the long `if/elif` chain with a lookup dictionary.

### Unit Converter
**What it does:** Converts between km/miles, kg/lbs, and meters/feet based on a menu choice.
**Why I built it:** To practice building a simple menu-driven program.
**What I'd do differently:** Store the conversions in a dictionary keyed by choice, and split each conversion into its own function.

### Calculator
**What it does:** Performs basic arithmetic with error handling for non-numeric input and division by zero.
**Why I built it:** My first real project — to practice `try/except` for input validation.
**What I'd do differently:** Add support for more operations (like exponents), and split the arithmetic into separate functions.

### Binary Search
**What it does:** Searches a sorted list for a target number by repeatedly cutting the remaining search range in half.
**Why I built it:** To implement a classic algorithm from scratch and understand why it runs in O(log n) instead of O(n).
**What I'd do differently:** My first version compared `mid` (a position) directly to the target value, instead of `list[mid]` (the value at that position). Fixed by indexing into the list correctly. Next time, I'd write it as a reusable function.

### Bank Account Simulation (OOP)
**What it does:** An `Account` class that models a bank account with overdraft protection and transaction history. A `SavingAccount` subclass extends it using inheritance.
**Why I built it:** My first real OOP project — to practice `class`, `__init__`, and `self`, and moving from function-based scripts to bundling data and behavior together.
**What I'd do differently:** After building it, I tested myself by closing the file and rewriting `deposit` and `withdraw` from memory. Two bugs showed up (dropped overdraft check, naming typo) which I fixed manually. Next time, I'd add a `transfer` method between two accounts.

### To-Do List Manager (OOP)
**What it does:** A command-line application using a custom class to manage state.
**Why I built it:** To reinforce OOP concepts by writing state logic entirely from scratch.
**What I'd do differently:** During development, I accidentally treated a list of strings like a list of dictionaries. Fixed by using Python's built-in `in` operator and `.remove()`. Next time, I'd add `.strip().lower()` for case-insensitive search.

---

## 🧩 LeetCode Practice (`leetcode/`)

| # | Problem | Approach | Result |
|---|---------|----------|--------|
| 001 | Two Sum | Brute force, nested loops | Accepted |
| 002 | Palindrome Number | Optimized: modulo/floor division, no string conversion | Accepted |
| 003 | Contains Duplicate | Hash set with early exit | Accepted, O(n) time/space |
| 004 | Valid Anagram | Hash map frequency counting | Accepted |
| 005 | Group Anagrams (Medium)| Sorted-word as dictionary key, grouping into lists | Accepted, beats 95% runtime |

*Note: All problems include a Problem Journal entry detailing the "what clicked" moment to bridge the gap between rote memorization and structural pattern recognition.*

---

## 🧠 Core Skills Demonstrated

*   **Data Science & Visualization:** Ingesting, cleaning, analyzing (`.groupby()`), and visualizing datasets using Pandas and Matplotlib.
*   **Repository Security:** Configuring a root-level `.gitignore` file to permanently protect the GitHub repository from bloated virtual environments (`env/`) and raw data files.
*   **API Integration & Networking:** Fetched and parsed live JSON data from external servers using the `requests` library and dynamic URLs.
*   **Environment Management:** Isolating project dependencies seamlessly using Python `venv`.
*   **File Handling (I/O):** Reading and writing external data using `csv` and plain text files.
*   **Data Structures:** Lists, nested dictionaries, tuples, sets, and 1D-to-2D grid mapping.
*   **Control Flow:** Complex loops (`for`, `while`, `for...else`) and conditional logic.
*   **Algorithms:** Implemented binary search from scratch (O(log n)). Solved 5 LeetCode problems independently, including a Medium with a top-5% runtime.
*   **Object-Oriented Programming (OOP):** Built robust classes with state management, inheritance (`super()`), and method overriding.
*   **Debugging & Self-Testing:** Verified OOP knowledge by rewriting code from memory without autocomplete; isolated and patched logic bugs independently.
*   **Mathematical Logic:** Hand-built truth tables and modeled basic discrete math concepts (AND/OR/NOT logic gates).
*   **Version Control:** Managing staging, commits, resolving merge conflicts, renaming remote repositories, and pushing entirely via the terminal.

## 🔜 Coming Next

*   **Data Science:** Performing data analysis on live Kaggle datasets.
*   **Algorithmic Patterns:** Mastering the Two Pointers technique on LeetCode.
*   **Applied Mathematics:** Expanding foundational Khan Academy linear algebra into vector matrices, transformations, and geometric calculus derivatives.
