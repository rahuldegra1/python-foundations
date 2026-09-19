from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("Data_Science/datasets/client_data.db")
    df = pd.read_sql_query("SELECT * FROM quotes_table", conn)
    conn.close()
    
    html_table = df.to_html(index=False, border=1)
    return render_template("index.html", table_data=html_table)

# --- NEW: Form Submission Backend ---
@app.route("/add", methods=["POST"])
def add_record():
    # 1. Grab the text the user typed into the browser form
    new_quote = request.form.get("quote")
    new_author = request.form.get("author")
    
    # 2. Connect to the database and INSERT the new row
    conn = sqlite3.connect("Data_Science/datasets/client_data.db")
    cursor = conn.cursor()
    # We use (?, ?) to securely inject the variables and prevent hackers from breaking the database
    cursor.execute("INSERT INTO quotes_table (Quote, Author) VALUES (?, ?)", (new_quote, new_author))
    conn.commit()
    conn.close()
    
    # 3. Force the browser to refresh the homepage to show the updated table
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)