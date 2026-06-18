import sqlite3
from config import DB_NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Table to store generated trading workflow steps
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trading_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            step_name TEXT NOT NULL,
            priority INTEGER,
            allocated_time INTEGER,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    
    # Table to log interaction data securely (Spreadsheet-mimic registry)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trade_registry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            strategy_prompt TEXT,
            action_logged TEXT
        )
    ''')
    conn.commit()
    conn.close()

def clear_previous_session():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM trading_tasks")
    conn.commit()
    conn.close()

def add_trading_step(step_name, priority, allocated_time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trading_tasks (step_name, priority, allocated_time) VALUES (?, ?, ?)", 
                   (step_name, priority, allocated_time))
    conn.commit()
    conn.close()

def get_active_workflow():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trading_tasks ORDER BY priority ASC, allocated_time ASC")
    steps = cursor.fetchall()
    conn.close()
    return steps

def register_interaction(strategy, action):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trade_registry (strategy_prompt, action_logged) VALUES (?, ?)", 
                   (strategy, action))
    conn.commit()
    conn.close()