# 🐍 Python Foundations

My programming work while pursuing an Online BCA at Manipal University Jaipur, built alongside a self-directed 3-year roadmap toward becoming an AI/ML engineer. Started August 2026.

This repository documents my progression from basic terminal scripts to object-oriented programming, local data science pipelines, and finally, live cloud-deployed web applications.

**Tech Stack:** Python 3, Flask, SQLite, Pandas, REST APIs (`requests`), HTML/CSS, Git, Render (Cloud Hosting).

---

## 🌐 Live Cloud Applications
*These full-stack web applications were built using Flask, styled with HTML/CSS, backed by SQLite databases, and deployed live to the public internet via Render.*

### 1. Financial Expense Tracker ([Live Demo](https://financial-expense-tracker-55kv.onrender.com))
* **What it does:** A production-ready financial dashboard that captures user expenses via HTML forms, permanently stores them in a cloud SQLite database, and dynamically calculates the total sum using Pandas (`df['amount'].sum()`). 
* **Why I built it:** To synthesize my roadmap skills into a final portfolio piece: database architecture (with automatic `init_db()` table generation), backend math logic, and cloud deployment via GitHub CI/CD.
* **What I'd do differently:** Group the expenses by category (`.groupby()`) and render a Matplotlib pie chart directly on the web page to visualize spending habits.

### 2. Global Weather App ([Live Demo](https://global-weather-app-uv6x.onrender.com))
* **What it does:** A cloud-deployed web app that chains two Open-Meteo REST APIs. It intercepts a user's city search, hits a Geocoding API to extract latitude/longitude, passes those coordinates to a Weather API, and renders the live temperature on a dark-mode frontend.
* **Why I built it:** To bypass hardcoded local datasets and integrate third-party REST APIs with a live Flask frontend. I defaulted initial testing to Tokyo to monitor conditions ahead of my first step to Japan.
* **What I'd do differently:** Add a 5-day forecast loop below the current temperature instead of just a single live reading.

### 3. Client Data Dashboard
* **What it does:** A local web application running on Flask that connects to a local SQLite database (`client_data.db`) to perform full CRUD operations (Create, Read, Update, Delete) and dynamically renders the data into an HTML table.
* **Why I built it:** To transition from local terminal scripts to live web servers, learning how to route URLs (`@app.route`) and intercept web form submissions (`POST`).
* **What I'd do differently:** Add user authentication so only authorized clients can view or manipulate the dashboard.

---

## 📊 Data Science Pipelines

### Regional Sales Pipeline (`002_pandas_load.py`)
* **What it does:** Ingests a raw `.csv` dataset, cleans text into `datetime64` time objects, runs a Split-Apply-Combine aggregation (`.groupby()`) to summarize regional revenue, and visualizes the math using a Matplotlib bar chart.
* **Why I built it:** To establish a fully functioning local Python data science environment, bypass Windows execution policies, and practice structural data analysis.
* **What I'd do differently:** Combine this logic with the `requests` library to pull and aggregate live data directly from the internet.

---

## 🖥️ Core Python Projects (Terminal & CLI)

<details>
<summary><strong>Object-Oriented Programming (OOP)</strong></summary>

* **Bank Account Simulation:** An `Account` class modeling a bank account with overdraft protection and transaction history, plus a `SavingAccount` subclass extending it via inheritance. *Reflection: Rewrote from memory to self-test; patched dropped overdraft checks independently.*
* **To-Do List Manager:** A command-line application using a custom class to manage state. *Reflection: Learned to differentiate between string lists and dictionary lists during state updates.*
</details>

<details>
<summary><strong>APIs & External Data</strong></summary>

* **User Lookup Tool:** Dynamically fetches and parses live JSON data from an external server using `requests`, injecting user input into the URL via f-strings.
* **Dynamic Quiz App:** A trivia game that reads questions, options, and correct answers from an external `questions.csv` file using `csv.DictReader`.
* **Contact Book:** Stores contacts as dictionaries in a list and persists data to a text file (`contact.txt`).
</details>

<details>
<summary><strong>Algorithmic Logic & Games</strong></summary>

* **Binary Search:** Searches a sorted list for a target number by cutting the range in half (O(log n) time complexity).
* **Tic-Tac-Toe:** A command-line 2-player game mapping a 3x3 grid to a 1D flat list (index 0-8) and checking 8 win combinations. 
* **Number Guessing Game:** Computer picks a random number; player has 7 attempts to guess with high/low hints.
* **Rock, Paper, Scissors:** Plays rounds against the computer using Python's `random` module, tracking session stats.
* **Calculator & Unit Converter:** Menu-driven programs performing basic arithmetic and unit conversions with `try/except` error handling for invalid user inputs.
</details>

---

## 🧩 Data Structures & Algorithms (LeetCode)

| # | Problem | Approach | Result |
|---|---------|----------|--------|
| 001 | Two Sum | Brute force, nested loops | Accepted |
| 002 | Palindrome Number | Optimized: modulo/floor division, no string conversion | Accepted |
| 003 | Contains Duplicate | Hash set with early exit | Accepted, O(n) time/space |
| 004 | Valid Anagram | Hash map frequency counting | Accepted |
| 005 | Group Anagrams (Medium)| Sorted-word as dictionary key, grouping into lists | Accepted, beats 95% runtime |
| 006 | Valid Palindrome | Two Pointers (Inward) | Accepted |
| 007 | Valid Parentheses | Stack (LIFO) with Dictionary | Accepted, 0ms runtime |
| 008 | Number of Recent Calls | Queue (FIFO) with Deque | Accepted, 40ms runtime |
| 009 | Two Sum II (Sorted) | Two Pointers (Opposite Ends), O(1) Space | Accepted, beats 81% runtime |
| 010 | Best Time to Buy/Sell Stock | Sliding Window (Dynamic Two Pointers) | Accepted, beats 96% memory |
| 011 | Fibonacci Number | Basic Recursion (Base Cases & Recursive Step) | Accepted |

*Note: All problems include a local Problem Journal entry detailing the "what clicked" moment to bridge the gap between rote memorization and structural pattern recognition.*

---

## 🧠 Core Skills Demonstrated

* **Full-Stack Web Development:** Engineered Flask routes, HTML/CSS templates, and `POST` form data interception.
* **Database Architecture:** Built SQLite databases, executed raw SQL CRUD operations, and wrote dynamic cloud initialization scripts (`CREATE TABLE IF NOT EXISTS`).
* **Cloud Deployment:** Configured production Gunicorn servers, locked `requirements.txt`, and launched live apps on Render via GitHub CI/CD.
* **Data Science:** Ingested, cleaned, grouped, and visualized datasets using Pandas and Matplotlib.
* **API Networking:** Fetched and parsed live nested JSON data from REST APIs.
* **Computer Science Fundamentals:** OOP (Classes, Inheritance, State), Binary Search implementations, and advanced algorithmic patterns (Hash Maps, Two Pointers, Sliding Window, Stacks, Queues, Recursion).
* **Environment Security:** Isolated dependencies via `venv` and protected root directories using `.gitignore`.

---

## 🔜 Coming Next
* **Data Science:** Performing data analysis on live Kaggle datasets.
* **Applied Mathematics:** Expanding foundational Khan Academy linear algebra into vector matrices, systems of linear equations, and determinants.
