import numpy as np
import sqlite3 as sql
from pathlib import Path

# -----------------------------
# Data Saving
# -----------------------------

def create_database(Database_filename):
    # Create the folder for the database path passed in from main.py.
    Path(Database_filename).parent.mkdir(parents=True, exist_ok=True)

    connection = sql.connect(Database_filename)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS model_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            elastic_thickness REAL,
            load_height REAL,
            load_width REAL,
            min_deflection REAL,
            flexural_rigidity REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_model_run(Database_filename, run_time, Te, load_height, load_width, deflection, D):
    # Save to the same database where create_database() created the table.
    connection = sql.connect(Database_filename)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO model_runs (
            elastic_thickness,
            load_height,
            load_width,
            min_deflection,
            flexural_rigidity
        )
        VALUES (?, ?, ?, ?, ?)
    """, (Te, load_height, load_width, float(np.min(deflection)), D))

    connection.commit()
    connection.close()